// import 'package:bloc/bloc.dart';
import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:lazy_load_scrollview/lazy_load_scrollview.dart';

import 'first/bloc/first_bloc.dart';


class FirstScriin extends StatelessWidget {
  const FirstScriin({Key? key}) : super(key: key);



  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('First Screen'),
      ),
      body: BlocBuilder<FirstBloc, FirstState>(builder: (context, state) {
        if (state is FirstInitial) {
          return const Center(
            child: CircularProgressIndicator(),
          );
        }
        if (state is FirstLoaded) {
          return _scrollView(context, state);
        }
        return const Center(
          child: CircularProgressIndicator(),
        );
      }),
    );
  }

  _scrollView(context, state) {
    // final FirstBloc _bloc = BlocProvider.of<FirstBloc>(context);
    return LazyLoadScrollView(
      onEndOfPage: () {
        // _bloc.add(AddFirst());
      },
      child: ListView.builder(
          itemCount: state.items.length,
          itemBuilder: (context, i) {
            return _itemsElement(context, state.items[i]);
          }),
    );
  }

  _itemsElement(context, element) {
    // final SecondBloc _bloc = BlocProvider.of<SecondBloc>(context);
    return GestureDetector(
        onTap: () {
        //   _bloc.add(LoadSecond(element.id));
        //   Navigator.push(
        //     context,
        //     MaterialPageRoute(builder: (context) => SecondScreen()),
        // );
        },
        child: Card(
          elevation: 2.0,
          margin: const EdgeInsets.symmetric(horizontal: 5, vertical: 3),
          child: Container(
            child: ListTile(
              title: Text(element.name.toString()),
              leading: CircleAvatar(child: Text(element.id.toString())),
            ),
          ),
        ),
    );
  }
}
