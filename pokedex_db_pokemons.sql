-- MySQL dump 10.13  Distrib 8.0.44, for Win64 (x86_64)
--
-- Host: localhost    Database: pokedex_db
-- ------------------------------------------------------
-- Server version	8.0.44

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `pokemons`
--

DROP TABLE IF EXISTS `pokemons`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pokemons` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(50) NOT NULL,
  `tipo1` varchar(20) NOT NULL,
  `tipo2` varchar(20) DEFAULT NULL,
  `treinador_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `treinador_id` (`treinador_id`),
  CONSTRAINT `pokemons_ibfk_1` FOREIGN KEY (`treinador_id`) REFERENCES `treinadores` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pokemons`
--

LOCK TABLES `pokemons` WRITE;
/*!40000 ALTER TABLE `pokemons` DISABLE KEYS */;
INSERT INTO `pokemons` VALUES (5,'Garchomp','Dragão','Terra',1),(6,'Garchomp','Dragão','Terra',2),(7,'Mimikyu','Fantasma','Fada',2),(8,'Golisopod','Inseto','Água',2),(9,'Khangaskan','Normal',NULL,2),(10,'Marshadow','Fantasma','Lutador',2),(11,'Vivillion','Inseto','Voador',2),(12,'Charizard','Fogo','Voador',3),(13,'Gengar','Fantasma','Venenoso',3),(14,'Alakazam','Psíquico',NULL,3),(15,'Mudkip','Elétrico','Grama',3),(16,'Hydregon','Sombrio','Dragão',3),(17,'Xerneas','Fada',NULL,3),(18,'Necrozma-dusk mane','Fada','Aço',4),(19,'Necrozma-dawn wings','Fada','Fantasma',4),(20,'Pikachu','Elétrico',NULL,4),(21,'Gardevoir','Psíquico','Fada',4),(22,'Krookodile','Sombrio','Terra',4),(23,'Kyurem-white','Dragão','Gelo',4);
/*!40000 ALTER TABLE `pokemons` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `treinadores`
--

DROP TABLE IF EXISTS `treinadores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `treinadores` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(100) NOT NULL,
  `cidade` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `treinadores`
--

LOCK TABLES `treinadores` WRITE;
/*!40000 ALTER TABLE `treinadores` DISABLE KEYS */;
INSERT INTO `treinadores` VALUES (1,'Lucas','Alola'),(2,'Davi','Eldorado do sul'),(3,'Anderson pilon','Itamaraju'),(4,'Erik schiavinato niza','Itatiba');
/*!40000 ALTER TABLE `treinadores` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-11-18 21:10:48
