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
            Tabela = pd.DataFrame(Dados, columns=Colunas)
            return Tabela

        Conexao.commit()
        return True

    except Exception as Erro:
        Conexao.rollback()
        st.error(f"Erro ao executar o comando: {Erro}")
        return None

    finally:
        Cursor.close()

def Inserir_Pokemon(NomePokemon, Tipo1, Tipo2):
    SQL = "Insert Into pokemons (nome, tipo1, tipo2) Values (%s, %s, %s)"
    return Executar_Comando(SQL, (NomePokemon, Tipo1, Tipo2))

def Pegar_Pokemons():
    SQL = "Select id, nome, tipo1, tipo2 From pokemons Order By id DESC"
    return Executar_Comando(SQL, Pegar_Dados=True)


def Tela_Cadastro():
    st.header("Cadastrar Pokémon")

    Tipos_Disponiveis = [
        "Normal", "Fogo", "Água", "Grama", "Elétrico", "Gelo",
        "Lutador", "Venenoso", "Terra", "Voador", "Psíquico",
        "Inseto", "Pedra", "Fantasma", "Dragão", "Aço", "Fada",
        "Sombrio", "Nenhum"
    ]

    Nome = st.text_input("Nome do Pokémon:")

    Coluna1, Coluna2 = st.columns(2)

    with Coluna1:
        Tipo1 = st.selectbox("Tipo Principal:", Tipos_Disponiveis[:-1])

    with Coluna2:
        Tipo2Escolhido = st.selectbox("Segundo Tipo:", Tipos_Disponiveis)
        if Tipo2Escolhido == "Nenhum":
            Tipo2Escolhido = None

    if st.button("Salvar Pokémon"):
        if Nome != "":
            Nome_Formatado = Nome.capitalize()
            Inserir_OK = Inserir_Pokemon(Nome_Formatado, Tipo1, Tipo2Escolhido)

            if Inserir_OK:
                st.success(f"Pokémon '{Nome_Formatado}' cadastrado com sucesso!")
        else:
            st.warning("Digite um nome, por favor.")


def Tela_Exebicao():
    st.header("Lista de Pokémons Cadastrados")

    TabelaPokemons = Pegar_Pokemons()

    if TabelaPokemons is None:
        return

    if TabelaPokemons.empty:
        st.info("Nenhum Pokémon Registrado no Momento!")
    else:
        TabelaPokemons.columns = ["ID", "Nome", "Tipo 1", "Tipo 2"]
        TabelaPokemons["Tipo 2"] = TabelaPokemons["Tipo 2"].fillna("—")

        st.dataframe(TabelaPokemons, use_container_width=True)

        Total = len(TabelaPokemons)
        st.caption(f"Total de Pokémon: {Total}")

def main():
    st.title("POKÉDEX — Sistema do Aluno")

    AbaCadastrar, AbaExebicao = st.tabs(["Cadastrar Pokémon", "Visualizar Pokémons"])

    with AbaCadastrar:
        Tela_Cadastro()

    with AbaExebicao:
        Tela_Exebicao()
        
main()
