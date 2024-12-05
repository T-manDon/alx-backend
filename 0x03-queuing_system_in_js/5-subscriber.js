import { createClient } from 'redis';

const redisClient = createClient();

//this func helps connect into the redis server
redisClient.on('connect', function () {
    console.log('Redis client connected to the server');
});

redisClient.on('error', function (error) {
    console.log(`Redis client not connected to the server: ${error.message}`);
});

//user can subscribe into the holberton school channel
redisClient.subscribe('holberton school channel');

//func helps to listen to system  messages channel and print them
redisClient.on('message', function (channel, message) {
  console.log(`${message}`);
  if (message === 'KILL_SERVER') {
//func to unsubscribe from channel and stop server conct
    redisClient.unsubscribe('holberton school channel');
    redisClient.end(true);
  }
});
