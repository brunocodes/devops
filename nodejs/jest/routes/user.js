const router = require('express').Router()

router.get('', (req, res) => {  
    res.json({
        user: "user"
    })
})

router.post('', (req, res) => {  
    res.status(201).json({
        user: "user"
    })
})

module.exports = router