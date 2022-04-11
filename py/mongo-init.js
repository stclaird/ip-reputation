conn = new Mongo();
db = conn.getDB("ip_reputation");

//lon then lat
db.col_ips.insert(
    {
        _id:        "1.11.62.187",
        ip_address: "1.11.62.187", 
        list_name:  "https://lists.blocklist.de/lists/all.txt" 
    }
 );
