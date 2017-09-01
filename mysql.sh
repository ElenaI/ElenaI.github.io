mysql -uroot -e "CREATE USER 'admin'@'localhost'"
mysql -uroot -e SET PASSWORD FOR  'admin'@'localhost' = PASSWORD('qwe')
mysql -uroot -e "CREATE DATABASE stepic"
mysql -uroot -e "GRANT ALL PRIVILEGES ON stepic.* TO 'admin'@'localhost'"