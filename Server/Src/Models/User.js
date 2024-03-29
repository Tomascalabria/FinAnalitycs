const mongoose=require('mongoose')


const userSchema = new mongoose.Schema({
    username: { type: String, required: true, unique: true },
    email: { type: String, required: true, unique: true },
    password: { type: String, required: true },
    isAdmin: { type: Boolean, default: false },
    profile_image: [],
    friends: [{ type: mongoose.Schema.Types.ObjectId, ref: 'User' }],
    splitwise: {
      oauth_token: String,
      oauth_verifier: String,
    },
  },
  {
    timestamps: true,
  });
  
  

module.exports=mongoose.model('User',userSchema)
