const router = require('express').Router()

router.get('', (req, res) => {  
    res.json({
        auth: 'auth'
    })
})

module.exports = router