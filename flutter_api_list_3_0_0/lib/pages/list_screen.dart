
import 'package:flutter/material.dart';
import 'package:flutter_api_1/first/bloc/first_bloc.dart';
import 'package:flutter_api_1/second/bloc/second_bloc.dart';
import 'package:flutter_bloc/flutter_bloc.dart';

import 'first_screen.dart';

class ListScreen extends StatelessWidget {
  const ListScreen({Key key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MultiBlocProvider(
      providers: [
        BlocProvider<FirstBloc>(
          create: (context) => FirstBloc()..add(InitialFirst()),
        ),
        BlocProvider<SecondBloc>(
          create: (context) => SecondBloc()..add(InitialSecond()),
        ),
      ],
      child: MaterialApp(
        title: 'BloC example',
        initialRoute: '/list_screen',
        onGenerateRoute: (routeSettings) {
          switch (routeSettings.name) {
            case '/list_screen':
              return MaterialPageRoute(
                  builder: (context) => const FirstScreen(), settings: routeSettings);
            default:
              return MaterialPageRoute(
                  builder: (context) => const FirstScreen(), settings: routeSettings);
              break;
          }
        },
      ),
    );
  }
}