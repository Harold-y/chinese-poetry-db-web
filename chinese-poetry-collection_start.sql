/*
 Navicat Premium Data Transfer

 Source Server         : CBRServer
 Source Server Type    : MySQL
 Source Server Version : 80020
 Source Host           : localhost:3306
 Source Schema         : chinese-poetry-collection

 Target Server Type    : MySQL
 Target Server Version : 80020
 File Encoding         : 65001

 Date: 03/10/2023 18:23:33
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for author
-- ----------------------------
DROP TABLE IF EXISTS `author`;
CREATE TABLE `author`  (
  `a_id` int(0) NOT NULL AUTO_INCREMENT,
  `a_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `a_dynasty_id` int(0) NULL DEFAULT NULL,
  `a_img_path` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`a_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 13627 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for collection
-- ----------------------------
DROP TABLE IF EXISTS `collection`;
CREATE TABLE `collection`  (
  `c_id` int(0) NOT NULL AUTO_INCREMENT,
  `c_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `c_note` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL,
  PRIMARY KEY (`c_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 9 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of collection
-- ----------------------------
INSERT INTO `collection` VALUES (6, '唐宋诗', '《全唐诗》是清康熙四十四年（1705年），彭定求、沈三曾、杨中讷、汪士鋐、汪绎、俞梅、徐树本、车鼎晋、潘从律、查嗣瑮10人奉敕编校，“得诗四万八千九百余首，凡二千二百余人”， 共计900卷，目录12卷。 来自百科\r\n\r\n《全宋诗》继唐诗的高度繁荣之后，宋诗在思想内容和艺术表现上有新的开拓和创造，出现了许多优秀作家作品，形成了许多流派，对元、明、清的诗歌发展产生了深远影响。来自百科');
INSERT INTO `collection` VALUES (7, '宋词', '《全宋词》是中国近百年来最重要的古籍整理成果之一。宋词和唐诗均为中国古典诗的艺术高峰。清代所编《全唐诗》是家喻户晓籍，现又新编出《全宋词》，堪称中国文学的双璧。全书共五册，荟萃宋代三百年间的词作。');
INSERT INTO `collection` VALUES (8, '诗经', '中国最早诗歌总集, 《诗经》，是中国古代诗歌开端，最早的一部诗歌总集，收集了西周初年至春秋中叶（前11世纪至前6世纪）的诗歌，共311篇，其中6篇为笙诗，即只有标题，没有内容，称为笙诗六篇（南陔、白华、华黍、由康、崇伍、由仪），反映了周初至周晚期约五百年间的社会面貌。');
INSERT INTO `collection` VALUES (9, '曹操诗集', '曹操喜欢用诗歌、散文来抒发自己政治抱负，反映民生疾苦，是魏晋文学的代表人物，其文学成就，\r\n主要表当今诗歌上，散文也很有特点。曹操的诗歌，今存20多篇，全部是乐府诗体。\r\n内容大体上可分三类。一类是关涉时事的，一类是以表述理想为主的，一类是游仙诗。');
INSERT INTO `collection` VALUES (10, '五代 南唐', '《南唐二主词》，系南唐中主李璟、后主李煜撰。约成书于南宋，后世续有辑补，又有后人编写了各种版本');
INSERT INTO `collection` VALUES (11, '五代 花间集', '《花间集》是中国五代十国时期编纂的一部词集，也是文学史上的第一部文人词选集，由后蜀人赵崇祚编辑。本书收录了温庭筠、韦庄等18位花间词派诗人的经典作品，集中而典型地反映了早期词史上文人词创作的主体取向、审美情趣、体貌风格和艺术成就。');
INSERT INTO `collection` VALUES (12, '元曲', '元曲，或称元杂剧，是盛行于元代的戏曲艺术，为散曲和杂剧的合称。相对于明朝的传奇（南曲），后世又将元曲称为北曲。元曲与宋词及唐诗、汉赋并称。');
INSERT INTO `collection` VALUES (13, '楚辞', '楚辞，有时也被称为骚体、楚辞体，是以屈原为代表的战国楚国诗人所创作的一种文体。');
INSERT INTO `collection` VALUES (14, '论语', '《论语》是以春秋时期思想家孔子言行为主的言论汇编，为儒家重要经典之一。');
INSERT INTO `collection` VALUES (15, '纳兰性德诗集', '纳兰性德（1655年-1685年），叶赫那拉氏，原名成德，避太子保成讳改名为性德，字容若，满洲正黄旗人，号楞伽山人。皇太子改名胤礽，才得以恢复。清朝著名词人，词风与李煜相似。纳兰出身显赫，父亲是康熙时期武英殿大学士纳兰明珠。纳兰性德自幼修文习武，康熙十五年（1676年）高中进士。初授三等侍卫，后晋为一等，长年被迫追随康熙左右。 纳兰性德生性淡泊名利，最擅写词。他的词以“真”取胜：写情真挚浓烈，写景逼真传神。纳兰性德在清初词坛独树一帜，词风“清丽婉约，哀感顽艳，格高韵远，独具特色，直指本心。”著有《通志堂集》、《侧帽集》、《饮水词》等，康熙二十四年（1685年）亡于寒疾，年仅三十一岁。被王国维称为“以自然之眼观物，以自然之舌言情”的词人。');

-- ----------------------------
-- Table structure for dynasty
-- ----------------------------
DROP TABLE IF EXISTS `dynasty`;
CREATE TABLE `dynasty`  (
  `d_id` int(0) NOT NULL AUTO_INCREMENT,
  `d_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `d_img_path` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`d_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 5 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of dynasty
-- ----------------------------
INSERT INTO `dynasty` VALUES (1, '唐朝', NULL);
INSERT INTO `dynasty` VALUES (2, '宋朝', NULL);
INSERT INTO `dynasty` VALUES (3, '元朝', NULL);
INSERT INTO `dynasty` VALUES (4, '五代', NULL);
INSERT INTO `dynasty` VALUES (5, '三国', NULL);
INSERT INTO `dynasty` VALUES (6, '春秋战国', NULL);
INSERT INTO `dynasty` VALUES (7, '清朝', NULL);

-- ----------------------------
-- Table structure for poetry
-- ----------------------------
DROP TABLE IF EXISTS `poetry`;
CREATE TABLE `poetry`  (
  `p_id` int(0) NOT NULL AUTO_INCREMENT,
  `p_title` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `p_author_id` int(0) NULL DEFAULT NULL,
  `p_rhythmic_id` int(0) NULL DEFAULT NULL,
  `p_paragraph` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL,
  `p_note` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL,
  `p_collection_id` int(0) NULL DEFAULT NULL,
  `p_other` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `p_img_path` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`p_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 332730 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for rhythmic
-- ----------------------------
DROP TABLE IF EXISTS `rhythmic`;
CREATE TABLE `rhythmic`  (
  `r_id` int(0) NOT NULL AUTO_INCREMENT,
  `r_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `r_note` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `r_img_path` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`r_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1452 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
