var express = require('express');
var router = express();
var MongoClient = require('mongodb').MongoClient;
var bodyParser = require('body-parser');
/* GET users listing. */

router.use(bodyParser.json());
router.use(bodyParser.urlencoded({ extended: false}));
// GET part of CRUD
router.get('/', function(req, res) {
 
// connect to the db
    MongoClient.connect("mongodb://nathanzm:nathanzm@ds047930.mongolab.com:47930/nathanzm", function(err, db) {
    if(err){
    res.send(err)
    }
    else{
    db.collection('proj',function(err,collection){
            if(err){
                return console.dir(err);

            }
            
            if('Rating' in req.query){req.query['Rating'] = (req.query["Rating"]);};
            if('Title' in req.query){req.query['Title'] = (req.query["Title"]);};
            if('Director' in req.query){req.query['Director'] = (req.query["Director"]);};
            if('Genre' in req.query){req.query['Genre'] = (req.query["Genre"]);};
            if('Run Time' in req.query){req.query['Run Time'] = (req.query["Run Time"]);};

            collection.find(req.query).toArray(function(err, docs){
               
                if(err){
                    return console.dir(err);
                }
                
                
                res.json(docs);
                db.close();
            });


            

    }); 





        


    }
    })

})
//Create part of CRUD
router.post('/', function(req, res){
    MongoClient.connect("mongodb://nathanzm:nathanzm@ds047930.mongolab.com:47930/nathanzm", function(err, db) {
        if(err){
            res.send(err)
        }
        else{
            db.collection('proj',function(err,collection){
            if(err){
                return console.dir(err);

            }

            var newMovie ={'Title': 'Movie',
                           'Director': 'Dude',
                           'Rating': '1.0',
                           'Run time': '0',
                           'Genre': 'shit'
                                         };

            if('Rating' in req.query){newMovie['Rating'] = (req.query['Rating']);};
            if('Title' in req.query){newMovie['Title'] = (req.query['Title']);};
            if('Director' in req.query){newMovie['Director'] = (req.query['Director']);};
            if('Genre' in req.query){newMovie['Genre'] = (req.query['Genre']);};
            if('Run time' in req.query){newMovie['Run time'] = (req.query['Run time']);};
            collection.insert(newMovie, function(err, hellaDope){
                if(err) {
                    return console.dir(err)
                };
                res.json(hellaDope);
                db.close();
                
            });


            });
        }
    });
});

//Delete part of CRUD

router.delete('/', function(req, res){

    MongoClient.connect("mongodb://nathanzm:nathanzm@ds047930.mongolab.com:47930/nathanzm", function(err, db) {
        if(err){
            res.send(err)
        }
        else{
            db.collection('proj',function(err,collection){
            if(err){
                return console.dir(err);

            }

            if('Rating' in req.query){req.query['Rating'] = (req.query['Rating']);};
            if('Title' in req.query){req.query['Title'] = (req.query['Title']);};
            if('Director' in req.query){req.query['Director'] = (req.query['Director']);};
            if('Genre' in req.query){req.query['Genre'] = (req.query['Genre']);};
            if('Run time' in req.query){req.query['Run time'] = (req.query['Run time']);};
            collection.remove(req.query, function(err, hellaDope){
                if(err) {
                    return console.dir(err)
                };
                res.json(hellaDope);
                db.close();
                
            });


            });
        }
    });
});


//Update part of CRUD
router.put('/', function(req, res){

    //Connect to the data base
    MongoClient.connect("mongodb://nathanzm:nathanzm@ds047930.mongolab.com:47930/nathanzm", function(err, db) {
    if(err){
    res.send(err)
    }
    else{
    db.collection('proj',function(err,collection){
            if(err){
                return console.dir(err);

            }
            
            if('Rating' in req.query){req.query['Rating'] = (req.query["Rating"]);};
            if('Title' in req.query){req.query['Title'] = (req.query["Title"]);};
            if('Director' in req.query){req.query['Director'] = (req.query["Director"]);};
            if('Genre' in req.query){req.query['Genre'] = (req.query["Genre"]);};
            if('Run Time' in req.query){req.query['Run Time'] = (req.query["Run Time"]);};

           var i = 0;
           for(var key in req.query)
           {

            if( i == 1)
                {break;}
            collection.update({key : req.query.key}, req.query, function(err, docs){
               
                if(err){
                    return console.dir(err);
                }
                
                
                res.json(docs);
                i++
                db.close();
                
            });
        }

            

    }); 





        


    }
    })

})


var server = router.listen(3000, function(){
    var host = server.address().address
    var port = server.address().port

    console.log("Example app listening at http://%s:%s", host, port)
})
//module.exports = router;