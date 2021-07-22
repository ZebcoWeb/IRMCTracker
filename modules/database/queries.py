CREATE_SERVERS_TABLE = """
    CREATE TABLE IF NOT EXISTS `servers`
    (
        `id`              INTEGER PRIMARY KEY AUTOINCREMENT,
        `name`            VARCHAR(50) NOT NULL UNIQUE,
        `address`         VARCHAR(50) NOT NULL UNIQUE,
        `current_players` INT(5) DEFAULT 0,
        `top_players`     INT(5) DEFAULT 0,
        `latest_version`  VARCHAR(200),
        `latest_latency`  INT(5) DEFAULT 0,
        `favicon`         VARCHAR(255),
        `discord`         VARCHAR(60)
    )"""

INSERT_SERVER = """
    INSERT INTO `servers`(
        name,
        address,
        current_players,
        top_players, 
        latest_version,
        latest_latency,
        favicon,
        discord
    ) 
    VALUES 
    (
        '%name%',
        '%address%',
        %current_players%,
        %top_players%, 
        '%latest_version%',
        '%latest_latency%',
        '%favicon%',
        '%discord%'
    )
"""

SELECT_SERVER_ALIKE_WITH_NAME = """
    SELECT * FROM `servers` WHERE name LIKE '%name%%'
"""

UPDATE_SERVER_WITH_NAME = """
    UPDATE `servers`
    SET current_players = %current_players%,
        top_players = %top_players%, 
        latest_version = '%latest_version%',
        latest_latency = '%latest_latency%',
        favicon = '%favicon%',
        discord = %discord%
    WHERE name = '%name%'
"""

SELECT_SERVER_WITH_NAME = """
    SELECT * FROM `servers` WHERE name = '%name%'
"""