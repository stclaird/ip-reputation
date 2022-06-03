conn = new Mongo();
db = conn.getDB("ip_reputation");

//Sample IP
db.col_ips.insert(
    {
        _id:        "1.11.62.187",
        ip_address: "1.11.62.187", 
        list_name:  "https://lists.blocklist.de/lists/all.txt" 
    }
 );

 //Load IP lists
 db.col_lists.insert(
     {
        _id: "blocklist.de",
        url: "https://lists.blocklist.de/lists/all.txt",
        type: "bot"
     },
     {
        _id: "torproject.org",
        url: "https://check.torproject.org/torbulkexitlist",
        type: "tor"
     }
 )