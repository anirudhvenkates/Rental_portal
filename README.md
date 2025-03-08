Added a README File
Test Ubuntu 24.04

wsl --list --verbose

wsl --unregister <DistroName>

wsl --install -d <DistroName>

sudo systemctl status mongod.service

MongoDB Enterprise Server - 8.0.5

MongoDB Shell - 2.4.0

MongoDB Commands:
mongsh
use mydb;
show dbs;
show collections;
db.myCollection.drop()
db.fs.files.find().pretty()

python Store_Files.py mydatabase /path/to/your/file.txt [your_filename_in_mongo.txt]
python Retrieve_Files.py mydatabase output.json
python Output_File_Data.py mydatabase your_filename.txt
python Delete_File.py mydatabase your_filename.txt

Create a user database
use users
db.users.insertOne({
    name: "Anirudh Venkatesh",
    ID: "S001",
    username: "anirudh",
    password: "password123",
    role: "Staff"
})
db.users.insertOne({
    name: "Anirudh Venkatesh",
    ID: "S002",
    username: "anirudh_v",
    password: "password123",
    role: "Customer"
})
db.users.find()
db.dropDatabase() 