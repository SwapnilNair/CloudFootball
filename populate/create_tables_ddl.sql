CREATE TABLE league
(
  league_id INT,
  league_name VARCHAR(64),
  country VARCHAR(64),
  sponsors VARCHAR(64),
  current_champions VARCHAR(64),
  top_scorer VARCHAR(64),
  PRIMARY KEY (league_id)
);

CREATE TABLE stadium
(
  stadium_id INT,
  stadium_name VARCHAR(64),
  city VARCHAR(64),
  surface_type VARCHAR(64),
  capacity INT,
  PRIMARY KEY (stadium_id)
);

CREATE TABLE team
(
  team_id INT,
  team_name VARCHAR(64),
  address VARCHAR(64),
  owners VARCHAR(64),
  trophies_won INT(64),
  league_id INT,
  stadium_id INT,
  PRIMARY KEY (team_id),
  FOREIGN KEY (league_id) REFERENCES league(league_id),
  FOREIGN KEY (stadium_id) REFERENCES stadium(stadium_id)
);

CREATE TABLE manager
(
  manager_id INT,
  manager_name_surname VARCHAR(64),
  nationality VARCHAR(64),
  manager_contract_start_date DATE,
  manager_contract_end_date DATE,
  age INT,
  team_id INT,
  PRIMARY KEY (manager_id),
  CHECK(manager_contract_end_date>manager_contract_start_date),
  FOREIGN KEY (team_id) REFERENCES team(team_id)
);

CREATE TABLE football_player
(
  player_id INT,
  player_name_surname VARCHAR(64),
  position VARCHAR(64),
  nationality VARCHAR(64),
  player_contract_start_date DATE,
  player_contract_end_date DATE,
  age INT,
  current_market_value FLOAT,
  team_id INT,
  PRIMARY KEY (player_id),
  CHECK(player_contract_end_date>player_contract_start_date),
  FOREIGN KEY (team_id) REFERENCES team(team_id)
);

CREATE TABLE player_statistics
(
  goals INT,
  assists INT,
  yellow_cards INT,
  red_cards INT,
  minutes_played INT,
  player_id INT,
  PRIMARY KEY (player_id),
  FOREIGN KEY (player_id) REFERENCES football_player(player_id)
);

CREATE TABLE referee
(
  license_number INT,
  referee_name_surname VARCHAR(64),
  classification VARCHAR(64),
  matches_refereed INT,
  league_id INT,
  PRIMARY KEY (license_number),
  FOREIGN KEY (league_id) REFERENCES league(league_id)
);

CREATE TABLE matches
(
  match_id INT,
  stadium VARCHAR(64),
  final_score VARCHAR(64),
  home_team VARCHAR(64),
  away_team VARCHAR(64),
  match_date DATE,
  license_number INT,
  league_id INT,
  PRIMARY KEY (match_id),
  FOREIGN KEY (license_number) REFERENCES referee(license_number),
  FOREIGN KEY (league_id) REFERENCES league(league_id)
);