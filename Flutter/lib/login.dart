import 'package:flutter/material.dart';

class loginpage extends StatefulWidget {
  @override
  _loginpageState createState() => _loginpageState();
}

class _loginpageState extends State<loginpage> {
  final _emailController = TextEditingController();
  final _passwordController = TextEditingController();

  @override
  void dispose() {
    _emailController.dispose();
    _passwordController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.green[100],
      
     
      body: Column(
        children: [
          Container( width: 300,height: 300,
            child: Image(image: AssetImage('assets/car.png'))),
          Padding(
            padding: const EdgeInsets.all(25.0),
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                TextField(
                  controller: _emailController,
                  decoration: InputDecoration( border: OutlineInputBorder(borderRadius: BorderRadius.circular(15)),
              filled: true,
             
              hintStyle: TextStyle(color: Colors.grey),
              fillColor: Colors.white,
                    labelText: 'Email',
                  ),
                ),
                SizedBox(height: 16),
                TextField(
                  controller: _passwordController,
                  obscureText: true,
                  decoration: InputDecoration(
                   border: OutlineInputBorder(borderRadius: BorderRadius.circular(15)),
              filled: true,
             
              hintStyle: TextStyle(color: Colors.grey),
              fillColor: Colors.white,
                    labelText: 'Password',
                  ),
                ),
                SizedBox(height: 16),
                ElevatedButton(
                  onPressed: () {
                    String email = _emailController.text;
                    String password = _passwordController.text;
                   
                    // Do something with email and password
                  },
                  child: Text('Submit'),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
