import 'package:flutter/material.dart';
import 'package:project2/userprofile.dart';

class homepage extends StatelessWidget {
  const homepage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.red,
        toolbarHeight: 50,
      ),
      body: SafeArea(
          child: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.start,
          children: [
            SizedBox(
              height: 20,
            ),
            Text(
              'VISION BASED PARKING BOOTH',
              style: TextStyle(fontWeight: FontWeight.bold, fontSize: 25),
            ),
            SizedBox(
              height: 100,
            ),
            Container(
              height: 70, width: 100,
              color: Colors.blue,
              //  decoration: BoxDecoration(borderRadius:  BorderRadius.all(Radius.circular(10.0))),

              child: new Center(
                  child: TextButton(
                onPressed: () {
                  Navigator.of(context).push(
                      MaterialPageRoute(builder: (context) => userprofile()));
                },
                child: Text('PROFILE',
                    style: TextStyle(
                        color: Colors.white,
                        fontSize: 15,
                        fontFamily: 'Times New Roman',
                        fontWeight: FontWeight.w700)),
              )),
            ),
            SizedBox(
              height: 20,
            ),
            Container(
              height: 70, width: 100,
              color: Colors.blue,
              //decoration: BoxDecoration(borderRadius:  BorderRadius.all(Radius.circular(5.0),)),
              child: new Center(
                  child: TextButton(
                onPressed: () {
                  Navigator.of(context).push(
                      MaterialPageRoute(builder: (context) => userprofile()));
                },
                child: Text('RECHARGE',
                    style: TextStyle(
                        color: Colors.white,
                        fontSize: 15,
                        fontFamily: 'Times New Roman',
                        fontWeight: FontWeight.w700)),
              )),
            )
          ],
        ),
      )),
    );
  }
}
