-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 17, 2025 at 04:36 AM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `mydompet`
--

-- --------------------------------------------------------

--
-- Table structure for table `debit`
--

CREATE TABLE `debit` (
  `debindex` int(11) NOT NULL,
  `UdateDebite` int(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `debit`
--

INSERT INTO `debit` (`debindex`, `UdateDebite`) VALUES
(1, 30000);

-- --------------------------------------------------------

--
-- Table structure for table `tunai`
--

CREATE TABLE `tunai` (
  `RanIndex` int(11) NOT NULL,
  `Pemasukan` int(50) NOT NULL,
  `Pengeluaran` int(50) NOT NULL,
  `Keterangan` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tunai`
--

INSERT INTO `tunai` (`RanIndex`, `Pemasukan`, `Pengeluaran`, `Keterangan`) VALUES
(2, 900, 0, 'test 4'),
(3, 5000, 100, 'test5'),
(4, 2000, 0, 'test6'),
(5, 289, 1, 'test7'),
(6, 8000, 90, 'test8'),
(7, 100, 100, 'final test'),
(8, 20, 10, 'final testlog'),
(9, 9000, 9000, 'final test with format'),
(10, 901, 1, 'tets aja'),
(11, 500, 500, 'tes lah'),
(12, 0, 0, 'final test');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `debit`
--
ALTER TABLE `debit`
  ADD PRIMARY KEY (`debindex`);

--
-- Indexes for table `tunai`
--
ALTER TABLE `tunai`
  ADD PRIMARY KEY (`RanIndex`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `debit`
--
ALTER TABLE `debit`
  MODIFY `debindex` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `tunai`
--
ALTER TABLE `tunai`
  MODIFY `RanIndex` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
