USE habi_db
CREATE TABLE IF NOT EXISTS likes (
    ID int(11) NOT NULL AUTO_INCREMENT, 
    property_id INT,
    auth_user_id INT, 
    given_on DATETIME
    PRIMARY KEY (ID)
    FOREIGN KEY (property_id) REFERENCES property(id)
    FOREIGN KEY (auth_user_id) REFERENCES auth_user(id)
)