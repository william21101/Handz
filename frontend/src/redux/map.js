import * as a from './actions/actions';
import * as th from './actions/thunks';

export const mapStateToProps = (state) => {
    return {
        token: state.token,
        username: state.username,
        chats: state.chats,
        is_logged_in: state.is_logged_in,
        userlist: state.userlist,
        tablelist: state.tablelist,
        hand: state.hand,
        seat: state.seat,
        table_id: state.table_id,
    };
};

export const mapDispatchToProps = (dispatch,emit) => {
    return {
      isLoggedIn: (bool) => {
        dispatch(a.isLoggedIn(bool))
      },
      modifyUserList: (logged_in,username) => {
        dispatch(a.modifyUserList(logged_in,username))
      },
      loginThunk: (username, password) => {
        dispatch(th.loginThunk(username,password));
      },
      logoutThunk: (token) => {
        dispatch(th.logoutThunk(token));
      },
      createUser: (username, password) => {
        dispatch(th.createUser(username,password));
      },
      chatThunk: (message, receiver) => {
        dispatch(th.chatThunk(message, receiver));
      },
      createTableThunk: () => {
        dispatch(th.createTableThunk());
      },
      joinTableThunk: (table_id) => {
        dispatch(th.joinTableThunk(table_id));
      },
      takeSeatThunk: (seat, table_id) => {
        dispatch(th.takeSeatThunk(seat, table_id));
      },
    }
};
