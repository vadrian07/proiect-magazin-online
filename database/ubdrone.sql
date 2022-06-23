-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Gazdă: 127.0.0.1:3306
-- Timp de generare: iul. 01, 2021 la 05:44 AM
-- Versiune server: 5.7.31
-- Versiune PHP: 7.3.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Bază de date: `ozifrumoasa`
--

-- --------------------------------------------------------

--
-- Structură tabel pentru tabel `admin`
--

DROP TABLE IF EXISTS `admin`;
CREATE TABLE IF NOT EXISTS `admin` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `numeadmin` varchar(125) NOT NULL,
  `email` varchar(100) NOT NULL,
  `parola` varchar(100) NOT NULL,
  `rol` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

--
-- Eliminarea datelor din tabel `admin`
--

INSERT INTO `admin` (`id`, `numeadmin`, `email`, `parola`, `rol`) VALUES
(5, 'admin', 'adrian@gmail.com', '$5$rounds=535000$Wf9M5/8opNvx5O6e$s8Xdw5.pFq4SLUWBlxX4yX4hxaD1GfSXii7X3pGUEr1', 'manager');

-- --------------------------------------------------------

--
-- Structură tabel pentru tabel `categorie_de_produs`
--

DROP TABLE IF EXISTS `categorie_de_produs`;
CREATE TABLE IF NOT EXISTS `categorie_de_produs` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `produs_id` int(11) NOT NULL,
  `FPV` varchar(10) NOT NULL DEFAULT 'no',
  `Air` varchar(10) NOT NULL DEFAULT 'no',
  `Mini2` varchar(10) NOT NULL DEFAULT 'no',
  `acc_air` varchar(10) NOT NULL DEFAULT 'no',
  `acc_dji_mavic` varchar(10) NOT NULL DEFAULT 'no',
  `acc_fpv` varchar(10) NOT NULL DEFAULT 'no',
  `brat_motor` varchar(10) NOT NULL DEFAULT 'no',
  `spare_arm` varchar(10) NOT NULL DEFAULT 'no',
  `ecoflow` varchar(10) NOT NULL DEFAULT 'no',
  `elistair` varchar(10) NOT NULL DEFAULT 'no',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=73 DEFAULT CHARSET=latin1;

--
-- Eliminarea datelor din tabel `categorie_de_produs`
--

INSERT INTO `categorie_de_produs` (`id`, `produs_id`, `FPV`, `Air`, `Mini2`, `acc_air`, `acc_dji_mavic`, `acc_fpv`, `brat_motor`, `spare_arm`, `ecoflow`, `elistair`) VALUES
(22, 22, 'no', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no'),
(23, 23, 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no'),
(24, 24, 'no', 'no', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no'),
(25, 25, 'no', 'no', 'no', 'yes', 'no', 'no', 'no', 'no', 'no', 'no'),
(26, 26, 'no', 'no', 'no', 'yes', 'yes', 'yes', 'no', 'no', 'no', 'no'),
(27, 27, 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no'),
(28, 28, 'no', 'no', 'no', 'yes', 'no', 'no', 'no', 'no', 'no', 'no'),
(29, 29, 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'yes', 'no', 'no'),
(30, 30, 'no', 'no', 'no', 'no', 'no', 'no', 'yes', 'no', 'no', 'no'),
(31, 31, 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'yes', 'no'),
(32, 32, 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'yes'),
(33, 33, 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no'),
(34, 34, 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no'),
(35, 35, 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no'),
(36, 36, 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no'),
(37, 37, 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no'),
(38, 38, 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no'),
(39, 39, 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no'),
(40, 40, 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no'),
(41, 41, 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no'),
(42, 42, 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no'),
(43, 43, 'no', 'no', 'no', 'yes', 'yes', 'yes', 'no', 'no', 'no', 'no'),
(44, 44, 'no', 'no', 'no', 'yes', 'yes', 'yes', 'no', 'no', 'no', 'no'),
(45, 45, 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no'),
(46, 46, 'no', 'no', 'no', 'no', 'no', 'yes', 'no', 'no', 'no', 'no'),
(47, 47, 'no', 'no', 'no', 'yes', 'yes', 'yes', 'no', 'no', 'no', 'no'),
(48, 48, 'no', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no'),
(49, 49, 'no', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no'),
(50, 50, 'no', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no'),
(51, 51, 'no', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no'),
(52, 52, 'no', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no'),
(53, 53, 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no'),
(54, 54, 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no'),
(55, 55, 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no'),
(56, 56, 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no'),
(57, 57, 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no'),
(58, 58, 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no'),
(59, 59, 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no'),
(60, 60, 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no'),
(61, 61, 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no'),
(62, 62, 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no'),
(63, 63, 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no'),
(64, 64, 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no'),
(65, 65, 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no'),
(66, 66, 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no'),
(67, 67, 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no'),
(68, 68, 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no'),
(69, 69, 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no'),
(70, 70, 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no'),
(71, 71, 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no'),
(72, 72, 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no');

-- --------------------------------------------------------

--
-- Structură tabel pentru tabel `comenzi`
--

DROP TABLE IF EXISTS `comenzi`;
CREATE TABLE IF NOT EXISTS `comenzi` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id_utilizator` int(11) DEFAULT NULL,
  `c_nume` text NOT NULL,
  `id_produs` int(11) NOT NULL,
  `cantitate` int(11) NOT NULL,
  `mplata` varchar(40) NOT NULL,
  `strada` text NOT NULL,
  `adr_loc` text NOT NULL,
  `telefon` varchar(15) NOT NULL,
  `dstatus` varchar(10) NOT NULL DEFAULT 'no',
  `data_comanda` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `data_livrare` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;

--
-- Eliminarea datelor din tabel `comenzi`
--

INSERT INTO `comenzi` (`id`, `id_utilizator`, `c_nume`, `id_produs`, `cantitate`, `mplata`, `strada`, `adr_loc`, `telefon`, `dstatus`, `data_comanda`, `data_livrare`) VALUES
(11, 16, 'Vasiliu Adrian', 22, 2, 'Ridicare personala', '8 Martie nr1 bl1 sc C ap 45', 'Bacau, Bacau', '0755756620', 'no', '2021-05-25 15:11:27', '2021-06-01'),
(12, NULL, 'Andrei Andrei', 34, 2, 'Livrare prin curier', '8 Martie nr 1 bl 1 sc c ap 45', 'Bacau', '0733424242', 'no', '2021-05-25 23:04:17', '2021-06-02'),
(13, 175, 'Vasiliu Adrian', 60, 2, 'Livrare prin curier', '8 Martie nr 1 bl 1 sc c ap 45', 'Bacau, Bacau', '0755756620', 'no', '2021-07-01 05:15:50', NULL);

-- --------------------------------------------------------

--
-- Structură tabel pentru tabel `produse`
--

DROP TABLE IF EXISTS `produse`;
CREATE TABLE IF NOT EXISTS `produse` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `p_nume` varchar(100) NOT NULL,
  `pret` int(11) NOT NULL,
  `descriere` text NOT NULL,
  `stoc` int(11) NOT NULL,
  `categorie` varchar(100) NOT NULL,
  `item` varchar(100) NOT NULL,
  `pcod` varchar(20) NOT NULL,
  `imagine` text NOT NULL,
  `c_data` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=73 DEFAULT CHARSET=latin1;

--
-- Eliminarea datelor din tabel `produse`
--

INSERT INTO `produse` (`id`, `p_nume`, `pret`, `descriere`, `stoc`, `categorie`, `item`, `pcod`, `imagine`, `c_data`) VALUES
(26, 'DJI Controller', 2999, 'DJI Smart Controller este echipat cu un ecran incorporat de 5 inch.', 2, 'Accesorii', 'Telecomanda', 'controller-25', 'telecomanda.jpg', '2021-05-25 15:26:10'),
(28, 'Geanta transport', 399, 'Lowepro Fastpack este un sling foto compact destinat calatoriilor datorita dimensiunii reduse. Acest sling foto Fastpack de la Lowepro este conceput pentru a gazdui un DSLR / MIrrorless impreuna cu 2-3 obiective.', 44, 'Accesorii', 'Lowepro Fastpack', 'wowepro-1', 'rucsac.jpg', '2021-05-25 15:30:37'),
(29, 'Elice Hurricane', 15, 'Gemfan Hurricane Durable 3 Blade. Elice personalizate, proiectate pentru pilotul de nivel superior, MCK.', 22, 'Piese', 'Gemfan Hurricane 51433', 'gemfan-514', 'elicedinplastic.jpg', '2021-05-25 15:31:49'),
(30, 'Brat cu motor ', 280, 'Brat spate dreapta cu motor.Piese originale DJI Mini 2.Pretul afisat este pentru o bucata', 12, 'Piese', 'Brat cu motor spate dreapta drona DJI Mavic Mini 2', 'brat-motor-2', 'motor-dreapta-drona.jpg', '2021-05-25 15:34:13'),
(31, 'Baterie ECOFLOW', 12000, 'EcoFlow Delta 1300 stabileste un nou standard pentru generatoarele de energie fara fir. Are o capacitate de 1260Wh, ceea ce il face cel mai avansat model al marcii EcoFlow.', 4, 'Baterii', 'Baterie Portabila EcoFlow Delta 1300', 'EcoFlow-2', 'alimentator-de-curent.jpg', '2021-05-25 15:35:44'),
(32, 'Elistair Baterie', 800, 'Safe-T este un tether station industrial inteligent, pentru UAV-uri. Ofera o capacitate de observare persistenta in timp real, cu o gama larga de compatibilitate. Acesta ofera: sistem patentat de management al legaturii inteligente, controlat de computer, complet programabil si actionabil de la distanta.', 6, 'Baterii', 'Safe-T Smart Tethered Station', 'Safe-T2', 'elistair.jpg', '2021-05-25 15:37:00'),
(33, 'Piesa Cadru Drona', 245, 'Cadru drona din fibra de carbon', 2, 'Piese', 'Piesa Cadru Carbo', 'c-c-2', 'cadru-drona-fibra-carbon.jpg', '2021-05-25 22:11:18'),
(58, 'DJI MAVIC', 5433, 'Zboara prin cer in moduri care par imposibile. Pasiunea pentru zbor e mereu cu noi si, cu DJI FPV, aceasta pasiune a transformat imaginatia in realitate.\r\n', 43, 'Drone', 'Drona', 'drona-22', 'drona2_1.jpg', '2021-06-30 21:17:17'),
(59, 'DJI MAVIC', 8422, 'Zboara prin cer in moduri care par imposibile. Pasiunea pentru zbor e mereu cu noi si, cu DJI FPV, aceasta pasiune a transformat imaginatia in realitate.\r\n', 44, 'Drone', 'Drona DJI FPV 2', 'drona-3', 'drona3.jpg', '2021-06-30 21:19:34'),
(60, 'DJI MAVIC', 2422, 'Zboara prin cer in moduri care par imposibile. Pasiunea pentru zbor e mereu cu noi si, cu DJI FPV, aceasta pasiune a transformat imaginatia in realitate.\r\n', 53, 'Drone', 'Drona DJI FPV 2', 'dji-222', 'dronaclasic4_2.jpg', '2021-06-30 21:38:50'),
(61, 'DJI Air2', 4242, 'Zboara prin cer in moduri care par imposibile. Pasiunea pentru zbor e mereu cu noi si, cu DJI FPV, aceasta pasiune a transformat imaginatia in realitate.\r\n', 22, 'Drone', 'drona air-2s', 'air-2ds2', 'drona-clasic2_1.png', '2021-06-30 21:40:45'),
(62, 'Baterie EcoFlow', 222, 'EcoFlow RIVER 370 RIVER 370 incheie epoca generatorului diesel zgomotos, greu si intepator. Unica fata de predecesorii si concurentii sai, Baterii externe - RIVER 370 Power Station este o cantitate industriala de putere, dar usoara, multifunctionala si usor de utilizat. Incarcati pana la 9 dispozitive simultan oriunde mergeti. Capacitate mare de 370WH - incorporata baterie de 370Wh (100000mAh la 3.7V), generatorul portabil va ofera o putere totala de 500W. ', 33, 'Baterii', 'baterie', 'baterie-2ss', 'alimentator-de-curent.jpg', '2021-06-30 21:42:59'),
(64, 'Baterie Safe-T', 242, 'EcoFlow RIVER 370 RIVER 370 incheie epoca generatorului diesel zgomotos, greu si intepator. Unica fata de predecesorii si concurentii sai, Baterii externe - RIVER 370 Power Station este o cantitate industriala de putere, dar usoara, multifunctionala si usor de utilizat. Incarcati pana la 9 dispozitive simultan oriunde mergeti. Capacitate mare de 370WH - incorporata baterie de 370Wh (100000mAh la 3.7V), generatorul portabil va ofera o putere totala de 500W. ', 2, 'Baterii', 'baterie-t', 'safe-t', 'elistair.jpg', '2021-06-30 21:44:46'),
(65, 'Amplificator', 2422, 'Amplificator Semnal Retea Wireless VAXIUJA,WiFi Repeater,transmisie 300Mbps,Retea 2.4G,Mod Repetor AP si Functia WPS,cu Port LAN de Antene Integrate', 22, 'Accesorii', 'accesoriu-drona', 'ddrona-accesori22', 'amplificator-antene.jpg', '2021-06-30 21:46:54'),
(66, 'VAXIUJA', 2233, 'Amplificator Semnal Retea Wireless VAXIUJA,WiFi Repeater,transmisie 300Mbps,Retea 2.4G,Mod Repetor AP si Functia WPS,cu Port LAN de Antene Integrate', 322, 'Accesorii', 'ACC-DRO', 'acc-dro2', 'amplificator-antene.jpg', '2021-06-30 21:47:27'),
(67, 'Piesa Joystick', 4242, 'Cea mai lina varianta de zbor Switchback\r\n\r\nPoate fi folosit cu elice de 6\", dar va recomandam 5.1\".', 22, 'Piese', 'piesa-joy', 'joy-2', 'joystick-control.jpg', '2021-06-30 21:49:12'),
(68, 'JoyStick', 222, 'Cea mai lina varianta de zbor Switchback\r\nPoate fi folosit cu elice de 6\", dar va recomandam 5.1\".', 22, 'Piese', 'piesa-2', 'peisa-22', 'motor-dreapta-drona.jpg', '2021-06-30 21:49:54'),
(69, 'Piesa Joystick', 334, 'Cea mai lina varianta de zbor Switchback\r\n\r\nPoate fi folosit cu elice de 6\", dar va recomandam 5.1\".', 22, 'Piese', 'Piesa-test', 'piesa-222', 'cadru-drona-fibra-carbon.jpg', '2021-06-30 21:50:24'),
(70, 'Drona UBD', 2322, 'DJI Mavic Air 2 DJI Mavic Air 2 Drona duce puterea si portabilitatea la nivelul urmator, oferind functii avansate intr-o forma compacta. Functiile de fotografiere inteligenta si calitate excelenta a imaginii pun capodoperele aeriene la indemana. Un zbor mai sigur si mai inteligent va permite sa va imbunatatiti si sa bucurati pe deplin de procesul creativ. ', 33, 'Drone', 'Mavic-Air2', 'mavic-air2', 'drona-clasic2_1.png', '2021-06-30 21:51:50'),
(71, 'Mavic2 AIR S', 4343, 'DJI Mavic Air 2 DJI Mavic Air 2 Drona duce puterea si portabilitatea la nivelul urmator, oferind functii avansate intr-o forma compacta. Functiile de fotografiere inteligenta si calitate excelenta a imaginii pun capodoperele aeriene la indemana. Un zbor mai sigur si mai inteligent va permite sa va imbunatatiti si sa bucurati pe deplin de procesul creativ. ', 333, 'Drone', 'drona-tt', 'cc-t', 'drona4.jpg', '2021-06-30 21:52:16'),
(72, 'MINI2', 533, 'DJI Mavic Air 2 DJI Mavic Air 2 Drona duce puterea si portabilitatea la nivelul urmator, oferind functii avansate intr-o forma compacta. Functiile de fotografiere inteligenta si calitate excelenta a imaginii pun capodoperele aeriene la indemana. Un zbor mai sigur si mai inteligent va permite sa va imbunatatiti si sa bucurati pe deplin de procesul creativ. ', 22, 'Drone', 'MINI2S', 'MINI2-S', 'drona-clasic.jpg', '2021-06-30 21:52:54');

-- --------------------------------------------------------

--
-- Structură tabel pentru tabel `utilizatori`
--

DROP TABLE IF EXISTS `utilizatori`;
CREATE TABLE IF NOT EXISTS `utilizatori` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(50) NOT NULL,
  `parola` varchar(100) NOT NULL,
  `data_inregistrare` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `online` varchar(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=178 DEFAULT CHARSET=latin1;

--
-- Eliminarea datelor din tabel `utilizatori`
--

INSERT INTO `utilizatori` (`id`, `email`, `parola`, `data_inregistrare`, `online`) VALUES
(176, '', '$5$rounds=535000$XTCXxQ2Z7Kdvak8F$Yo4eZInNJP0VnA8vazugRL6eUXHF7gI9y3jNFZwuiw8', '2021-07-01 05:19:46', '0'),
(177, 'test3@yahoo.com', '$5$rounds=535000$GbB2/1MTELjqmlXL$lBbt2qYv4pmN.jp7KdX2QqBErOlUyKyprdsmuyLvWD9', '2021-07-01 05:43:40', '1');

-- --------------------------------------------------------

--
-- Structură tabel pentru tabel `vizualizare_produs`
--

DROP TABLE IF EXISTS `vizualizare_produs`;
CREATE TABLE IF NOT EXISTS `vizualizare_produs` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `utilizator_id` int(11) NOT NULL,
  `produs_id` int(11) NOT NULL,
  `c_data` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=54 DEFAULT CHARSET=latin1;

--
-- Eliminarea datelor din tabel `vizualizare_produs`
--

INSERT INTO `vizualizare_produs` (`id`, `utilizator_id`, `produs_id`, `c_data`) VALUES
(53, 175, 60, '2021-07-01 05:15:24'),
(52, 174, 71, '2021-06-30 21:53:24'),
(51, 174, 72, '2021-06-30 21:53:17'),
(50, 174, 63, '2021-06-30 21:44:59'),
(49, 174, 61, '2021-06-30 21:40:53'),
(48, 174, 60, '2021-06-30 21:38:55'),
(47, 174, 59, '2021-06-30 21:27:48'),
(46, 174, 58, '2021-06-30 21:17:26'),
(45, 174, 24, '2021-06-30 21:06:45'),
(44, 174, 23, '2021-06-30 21:06:13'),
(43, 174, 22, '2021-06-30 21:05:40'),
(42, 174, 27, '2021-06-30 21:05:06'),
(41, 174, 25, '2021-06-30 21:04:58'),
(34, 99, 36, '2021-06-03 14:11:25'),
(35, 99, 37, '2021-06-03 14:13:33'),
(36, 204, 22, '2021-06-25 11:50:09'),
(37, 204, 23, '2021-06-25 11:55:52'),
(38, 168, 50, '2021-06-28 15:12:53'),
(39, 174, 39, '2021-06-30 20:05:02'),
(40, 174, 53, '2021-06-30 20:59:47');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
