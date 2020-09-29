const express = require('express')
const bodyParser= require('body-parser')
const app = express()
const MongoClient = require('mongodb').MongoClient

MongoClient.connect('mongodb+srv://@cluster0.xjgk2.mongodb.net/?retryWrites=true&w=majority',
{useUnifiedTopology: true},
   (err, client) => {
    if (err) return console.error(err)
    console.log('Yhteys MongoDB:n luotu')
    const db = client.db('annikan-harkka')
    const tietopankki = db.collection('tietopankki')
  
    app.listen(3000, function(){
    console.log('kuuntelen porttia 3000')
        })
    app.use(bodyParser.urlencoded({ extended: true }))

    app.set('view engine', 'ejs')

    
    app.get('/', (req, res) => {
         db.collection('tietopankki').find().toArray()
         .then(results => {
            res.render('index.ejs', {tietopankki: results })
         })
           .catch(error => console.error(error))
           
            
          })

    app.post('/quotes', (req, res) => {
        tietopankki.insertOne(req.body)
        .then(result =>{
            res.redirect('/')
        })
        .catch(error => console.error(Error))
        })
    })