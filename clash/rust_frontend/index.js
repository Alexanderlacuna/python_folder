import fetch from 'cross-fetch'

async function get_user_with_public(){


	try{
		const res=await fetch(`http://localhost:3000/user2/getUser?id=${1}`)
		let data=await res.json()
		// console.log(data)
		// let k=await token_validity(data)
	}
	catch(err){
		console.log(err)
	}
}

async function token_validity(token){



	try{
		let res=await fetch (`http://localhost:3000/user/testLogin?auth_token=${token}`)
		console.log(res)
		console.log(res.body)
	    var  data=await res.text();

	    console.log(data)


	}catch(err){
		console.log(err)
	}

	return data
	
}

async function getUsers(){
	try{
       const res=await fetch("http://localhost:3000/user/getUsers");

       const data=await res.json()
       console.log(data)
       // console.log(data)
	}
	catch(err){
		console.log(err)

	}


}

async function login(username,email){

	var found=""
	try{
	   let res=await fetch("http://localhost:3000/user/login",{
		method:"POST",
		headers: { 'Content-Type': 'application/json' },
		body:JSON.stringify({username,email})
	})
	   console.log(res)

	 let data=await res.json()
	 let b=data.auth_token
	 console.log(b) 

	 // found=await data
	 await token_validity(b)
	 // found=data

	}

	catch(err){

		console.log(err)

	}
	return await found

}


async function registerUser(username,email){
	let userData={
		username:username,
		email:email
	}

	console.log(userData)

	try{

		let res=await fetch("http://localhost:3000/user/createUser",{
		method:"POST",
		headers: { 'Content-Type': 'application/json' },
		body:JSON.stringify(userData)
	})

		

		

	}
	catch(err){
		console.log(err.response)
	}
	

	
}
// console.log(getUsers())

let t='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJhbGV4YW5kZXJrYWJ1YUBnbWFpbC5jb20iLCJjb21wYW55IjoiZHNmc2RmIiwiZXhwIjoxNTk2ODEzNDAwfQ.qCsUl3t6um3s5O3cjLpluulKOtMSzQppOLMZ8KxNHVg'
let r=login("alexis","alexanderkabua@gmail.com")

get_user_with_public()

token_validity('d').then((data)=>console.log(data))
// registerUser("Javascript","js@gmail.com")
// loaderio-14e2c7818404ec4d27bfcc67fc7bec64