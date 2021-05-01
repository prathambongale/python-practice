import motor.motor_tornado
import tornado.ioloop

client = motor.motor_tornado.MotorClient(
   'mongodb://localhost:27017')
db = client['reactive-services']

userCollection = db['users']

async def do_count():
    n = await userCollection.count_documents({})
    print('%s documents in collection' % n)
    n = await userCollection.count_documents({'i': {'$gt': 1000}})
    print('%s documents where i > 1000' % n)


#IOLoop.current().run_sync(do_count)

tornado.ioloop.IOLoop.current().run_sync(do_count)

