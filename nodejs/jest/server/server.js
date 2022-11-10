const express = require('express')
const PORT = process.env.PORT || 5000

const app = express()
app.use(express.json())

app.get('/status',(req, res) => { res.status(200).json({}) })
app.use('/users', require('../routes/user'))
app.use('/auth', require('../routes/auth/auth'))

if (process.env.NODE_ENV !== 'test') {
    app.listen( PORT, () => console.log(`* server started on port ${PORT}`))
}

module.exports = { app }