const request = require('supertest');
const { app } = require('../../server/server')

describe('Test user route', () => {
  test('It should response 200', async () => {
    const response = await request(app).get('/users')
    expect(response.statusCode).toBe(200)
  })
})