import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';

import 'first/bloc/first_bloc.dart';
import 'first_screen.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {


 


  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MultiBlocProvider(
      providers: [
        BlocProvider<FirstBloc>(
          create: (context) => FirstBloc(_)..add(InitialFirst()),
        ),
        // BlocProvider(
        //   create: (context) => FirstBloc(),
        // ),
      ],
      child: MaterialApp(
        title: 'Bloc Example',
        initialRoute: '/',
        onGenerateRoute: (routeSettings) {
          switch (routeSettings.name) {
            case '/':
              return MaterialPageRoute(
                  builder: (context) => const FirstScriin(), settings: routeSettings);
            default:
              return MaterialPageRoute(
                  builder: (context) => const FirstScriin(), settings: routeSettings);
          }
        },
      ),
    );
  }
}