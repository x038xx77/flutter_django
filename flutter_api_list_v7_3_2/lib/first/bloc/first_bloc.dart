import 'package:bloc/bloc.dart';
import 'package:flutter_api_v7_3_2/model/item_user.dart';
import 'package:http_auth/http_auth.dart';
import 'package:meta/meta.dart';

part 'first_event.dart';
part 'first_state.dart';

// class FirstBloc extends Bloc<FirstEvent, FirstState> {
//   FirstBloc() : super(FirstInitial()) {
//     on<FirstEvent>((event, emit) {
//       // ignore: todo


//     });

class FirstBloc extends Bloc<FirstEvent, FirstState> {
  List<ItemUser> items = [];
  int _page = 0;

  FirstBloc(FirstState initialState) : super(initialState);


  @override
  FirstState get initialState => FirstInitial();

  @override
  Stream<FirstState> mapEventToState(
    FirstEvent event,
  ) async* {
    if (event is InitialFirst) {
      yield FirstInitial();
      for (int _i = 1; _i < 7; _i++) {
        _page = _i;
        await _fetch(_page);
        yield FirstLoaded(items);
      }
    }
    if (event is AddFirst) {
      await _fetch(++_page);
      yield FirstLoaded(items);
    }
  }

  Future _fetch(_page) async {
    final _client = BasicAuthClient('', '');
    final url = Uri.parse('https://jsonplaceholder.typicode.com/comments/$_page');
    // print(await http.read(Uri.parse('https://jsonplaceholder.typicode.com/comments/')));

    final _response = await _client
        .get(url);
    final _result = itemUserFromJson(_response.body);
    items.add(_result);
  }
}

