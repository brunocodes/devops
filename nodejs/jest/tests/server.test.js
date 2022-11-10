const request = require('supertest');
const { app } = require('../server/server')

describe('Test API status', () => {
  test('It should response 200', async () => {
    const response = await request(app).get('/status')
    expect(response.statusCode).toBe(200)

    //   .then((response) => {
    //     expect(response.statusCode).toBe(200)
    //     done()
    // })
  })
})

// describe('test server health', () => {
//     test('ping status', () => {
//       expect(true).toBeTruthy();
//     })
  
//     // test('is not sour', () => {
//     //   expect(false).toBeFalsy();
//     // });
// })