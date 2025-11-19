import streamlit as st
import mysql.connector
import pandas as pd

HOST = "localhost"
USER = "root"
PASSWORD = "#2008vida"
DATABASE = "pokedex_db"

def Conectar_Banco():
    try:
        Conexao = mysql.connector.connect(
            host=HOST,
            user=USER,
            password=PASSWORD,
            database=DATABASE
        )
        return Conexao
    except:
        st.error("Não foi possível Conectar com o Banco de Dados.")
        return None

def Executar_Comando(SQL_Comando, Valores=None, Pegar_Dados=False):
    Conexao = Conectar_Banco()

    if Conexao is None:
        return None

    Cursor = Conexao.cursor()

    try:
        Cursor.execute(SQL_Comando, Valores)

        if Pegar_Dados:
            Dados = Cursor.fetchall()
            Colunas = [c[0] for c in Cursor.description]
            return pd.DataFrame(Dados, columns=Colunas)

        Conexao.commit()
        return True

    except Exception as Erro:
        Conexao.rollback()
        st.error(f"Erro ao executar o comando: {Erro}")
        return None

    finally:
        Cursor.close()

def Inserir_Treinador(Nome, Cidade):
    SQL = "INSERT INTO treinadores (nome, cidade) VALUES (%s, %s)"
    return Executar_Comando(SQL, (Nome, Cidade))

def Pegar_Treinadores():
    SQL = "SELECT id, nome, cidade FROM treinadores ORDER BY nome ASC"
    return Executar_Comando(SQL, Pegar_Dados=True)

def Inserir_Pokemon(NomePokemon, Tipo1, Tipo2, TreinadorID):
    SQL = "INSERT INTO pokemons (nome, tipo1, tipo2, treinador_id) VALUES (%s, %s, %s, %s)"
    return Executar_Comando(SQL, (NomePokemon, Tipo1, Tipo2, TreinadorID))

def Pegar_Pokemons():
    SQL = """
        SELECT p.id, p.nome, p.tipo1, p.tipo2, t.nome AS treinador
        FROM pokemons p, treinadores t
        WHERE p.treinador_id = t.id
        ORDER BY p.id DESC;
    """
    return Executar_Comando(SQL, Pegar_Dados=True)

def Tela_Treinador():
    st.header("Cadastrar Treinador")

    Nome = st.text_input("Nome do Treinador:")
    Cidade = st.text_input("Cidade de Origem:")

    if st.button("Salvar Treinador"):
        if Nome != "" and Cidade != "":
            OK = Inserir_Treinador(Nome.capitalize(), Cidade.capitalize())
            if OK:
                st.success(f"Treinador '{Nome}' cadastrado com sucesso!")
        else:
            st.warning("Preencha todos os campos.")

def Tela_Cadastro():
    st.header("Cadastrar Pokémon")

    Tipos = [
        "Normal", "Fogo", "Água", "Grama", "Elétrico", "Gelo",
        "Lutador", "Venenoso", "Terra", "Voador", "Psíquico",
        "Inseto", "Pedra", "Fantasma", "Dragão", "Aço", "Fada",
        "Sombrio", "Nenhum"
    ]

    Nome = st.text_input("Nome do Pokémon:")

    Coluna1, Coluna2 = st.columns(2)

    with Coluna1:
        Tipo1 = st.selectbox("Tipo Principal:", Tipos[:-1])

    with Coluna2:
        Tipo2Selecionado = st.selectbox("Segundo Tipo:", Tipos)
        if Tipo2Selecionado == "Nenhum":
            Tipo2Selecionado = None

    Treinadores = Pegar_Treinadores()

    if Treinadores is None or Treinadores.empty:
        st.warning("Cadastre um treinador antes de cadastrar Pokémon!")
        return

    ListaNomes = Treinadores["nome"].tolist()
    Escolhido = st.selectbox("Treinador Responsável:", ListaNomes)

    TreinadorID = int(Treinadores[Treinadores["nome"] == Escolhido]["id"].iloc[0])

    if st.button("Salvar Pokémon"):
        if Nome != "":
            OK = Inserir_Pokemon(Nome.capitalize(), Tipo1, Tipo2Selecionado, TreinadorID)
            if OK:
                st.success(f"Pokémon '{Nome}' cadastrado com sucesso!")
        else:
            st.warning("Digite um nome.")

def Tela_Exebicao():
    st.header("Pokémons Cadastrados")
    Tabela = Pegar_Pokemons()

    if Tabela is None:
        return
    
    if Tabela.empty:
        st.info("Nenhum Pokémon Registrado!")
    else:
        Tabela.columns = ["ID", "Nome", "Tipo 1", "Tipo 2", "Treinador"]
        Tabela["Tipo 2"] = Tabela["Tipo 2"].fillna("—")

        st.dataframe(Tabela, use_container_width=True)

        st.caption(f"Total de Pokémon: {len(Tabela)}")

def main():
    st.title("POKÉDEX ")
    AbaTreinador, AbaCadastrar, AbaExebicao = st.tabs(["Cadastrar Treinador","Cadastrar Pokémon","Visualizar Pokémons"])

    with AbaTreinador:
        Tela_Treinador()

    with AbaCadastrar:
        Tela_Cadastro()

    with AbaExebicao:
        Tela_Exebicao()

main()
