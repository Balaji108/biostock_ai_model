
let Block = require('./block')
let Blockchain = require('./blockchain')
let BlockchainNode = require('./BlockchainNode')
let Transaction = require('./transaction')
let sha256 = require('js-sha256')
let DrivingRecordSmartContract = require('./smartContracts')

let fetch = require('node-fetch')

const express = require('express')
const app = express()
const bodyParser = require('body-parser')

let port = 3000

// access the arguments
process.argv.forEach(function(val,index,array){
  port = array[2]
})

if(port == undefined) {
  port = 3000
}

let transactions = []
let nodes = []
let genesisBlock = new Block()
let blockchain = new Blockchain(genesisBlock)

app.use(bodyParser.json())

app.get('/resolve',function(req,res){

  nodes.forEach(function(node){

      fetch(node.url + '/blockchain')
      .then(function(response){
        return response.json()
      })
      .then(function(otherNodeBlockchain){

          if(blockchain.blocks.length < otherNodeBlockchain.blocks.length) {
            blockchain = otherNodeBlockchain
          }

          res.send(blockchain)

      })

  })

})

app.post('/nodes/register',function(req,res){

  let nodesLists = req.body.urls
  nodesLists.forEach(function(nodeDictionary){
    let node = new BlockchainNode(nodeDictionary["url"])
    nodes.push(node)
  })

  res.json(nodes)

})

app.get('/nodes',function(req,res){
  res.json(nodes)
})

app.get('/',function(req,res){
  res.send("hello world")
})

app.get('/mine',function(req,res){

    let block = blockchain.getNextBlock(transactions)
    blockchain.addBlock(block)
    transactions = []
    console.log(transactions)
    res.json(block)
})

// driving-records/TX1234
// driving-records/CA1234
app.get("/stocks",function(req,res){

  let stockname = req.query.stockname
  let transactions = blockchain.transactionsByStock(stockname)
  
  res.json(transactions)

})

app.post('/transactions',function(req,res){

  console.log("sujeet")

  let stockName = req.body.stockName
  let stockPrice = req.body.stockPrice
  let agentName =  req.body.agentName

  let transaction = new Transaction(stockName,stockPrice,agentName)

  transactions.push(transaction)

  res.json(transactions)

})

app.get('/blockchain',function(req,res){

  res.json(blockchain)

})

app.listen(port,function(){
  console.log("server has started")
})



