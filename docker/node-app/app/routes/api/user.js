const router = require('express').Router()
// const passport  = require('passport');
// require('dotenv').config();
// const CLIENT_DASH_PAGE_URL = process.env.CLIENT_DASH_PAGE_URL; 
// const CLIENT_HOME_PAGE_URL = process.env.CLIENT_HOME_PAGE_URL;

const checkPeram = (req, res, next) => {
  const reqQuery = req.query
  if(!reqQuery){
    res.status(400).send('Bad Request')
  } else if(req.user) {
    next()
  }
}

const PREFIX = "/v1/users"

// @route   POST /users
// @desc    Create new user
// @access  Public
router.post(PREFIX, (req, res) => {  
  const user = req.body.user
  res.json({
    ...user
  })
})

// @route   GET /users
// @desc    Get user by ID.
// @access  Public 
router.get(`${PREFIX}/:id`, (req, res) => {
  const userID = req.query.id
  res.json({
    user: "User1",
    user_id: userID
  })
})

// @route   PUT /users
// @desc    Get user by ID.
// @access  Public 
router.put(`${PREFIX}/:id`, checkPeram, (req, res) => {
  const user = req.body.user
  res.json({
    user: user
  })
})

// @route   DELETE /users
// @desc    Get user by ID.
// @access  Public 
router.delete(`${PREFIX}/:id`, checkPeram, (req, res) => {
  const user = req.body.user
  res.json({
    user: user
  })
})

module.exports = router