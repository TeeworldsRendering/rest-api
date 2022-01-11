CREATE TABLE IF NOT EXISTS `skin` (
    `guild_id` VARCHAR(20),
    `user_id` VARCHAR(20),
	`filename` VARCHAR(100),
    `md5_checksum` VARCHAR(35),
    UNIQUE KEY `guild_id` (`guild_id`, `filename`)
) CHARACTER SET ascii COLLATE ascii_general_ci;