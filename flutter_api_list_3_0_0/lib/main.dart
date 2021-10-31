import 'package:flutter/material.dart';
import 'package:flutter_api_1/pages/about.dart';

import 'pages/details.dart';
import 'pages/home.dart';
import 'pages/list_screen.dart';


main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'TestAPPLPA',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        primarySwatch: Colors.blue,
        visualDensity: VisualDensity.adaptivePlatformDensity,
      ),
      initialRoute: '/home',
      routes: <String, WidgetBuilder>{
        '/home': (BuildContext context) => Home(),
        '/details': (BuildContext context) => Details(),
        '/about': (BuildContext context) => About(),
        '/list_screen': (BuildContext context) => const ListScreen(),
      },
    );
  }
}
