import * as a from 'redux/actions/actionTypes';
import {combineReducers} from "redux";

export const initialState = {};

export const token = (state = "", action) => {
    switch(action.type) {
        case a.GET_TOKEN:
            return action.token;
        default:
            break;
    }
    return state;
}

export const username = (state = '', action) => {
    switch(action.type) {
        case a.GET_USERNAME:
            return action.username;
        default:
            break;
    }
    return state;
}

export const chats = (state = [], action) => {
    switch(action.type) {
        case a.CHAT_MESSAGE:
            let chat = action.message
            return [...state, chat];
        default:
            break;
    }
    return state;
}

export const is_logged_in = (state = false, action) => {
    switch(action.type) {
        case a.IS_LOGGED_IN:
            return action.bool;
        default:
            break;
    }
    return state;
}

export const userlist = (state = [], action) => {
    switch(action.type) {
        case a.MODIFY_USER_LIST:
            switch(action.is_logged_in) {
                case true:
                    // console.log(state)
                    // console.log(action.users)
                    // console.log(state.length)
                    if (state.length === 0) {
                        return action.users;
                    }
                    else {
                      return [...state, action.username]
                    }
                case false:
                    let temp = Object.assign([],state);
                    console.log(temp)
                    temp.splice(temp.indexOf(action.username),1);
                    return temp;
                default:
                    break;
            }
        default:
            break;
    }
    return state;
}

export const tablelist = (state = [], action) => {
    switch(action.type) {
        case a.CREATE_TABLE:
            return [...state,action.id];
        case a.GET_TABLES:
            return action.tablelist;
        default:
            break;
    }
    return state;
}

export const hand = (state = {'spades': '', 'hearts': '',
                            'diamonds': '', 'clubs': ''}, action) => {
    switch(action.type) {
        case a.GET_HAND:
            return action.hand;
        case a.LEAVE_SEAT:
            return {'spades': '', 'hearts': '',
                                        'diamonds': '', 'clubs': ''};
        case a.LEAVE_TABLE:
            return {'spades': '', 'hearts': '',
                                        'diamonds': '', 'clubs': ''};
        default:
            break;
    }
    return state;
}

export const seat = (state = '', action) => {
    switch(action.type) {
        case a.TAKE_SEAT:
            return action.seat;
        case a.LEAVE_SEAT:
            return '';
        case a.LEAVE_TABLE:
            return '';
        default:
            break;
    }
    return state;
}

export const direction_to_act = (state = '', action) => {
    switch(action.type) {
        case a.GET_NEXT_ACTOR:
          return action.direction_to_act;
        case a.LEAVE_TABLE:
            return '';
        default:
            break;
    }
    return state;
}

export const auction = (state = [], action) => {
    switch(action.type) {
        case a.GET_AUCTION:
          return action.auction;
        case a.LEAVE_TABLE:
            return [];
        default:
            break;
    }
    return state;
}

export const contract = (state = '', action) => {
    switch(action.type) {
        case a.GET_CONTRACT:
          return action.contract;
        case a.LEAVE_TABLE:
            return '';
        default:
            break;
    }
    return state;
}

const empty_trick = {'north': '', 'south': '', 'east': '', 'west': ''}

export const trick = (state = empty_trick, action) => {
    switch(action.type) {
        case a.GET_TRICK:
          return action.trick;
        case a.LEAVE_TABLE:
            return empty_trick;
        default:
            break;
    }
    return state;
}

export const suit_led = (state = '', action) => {
    switch(action.type) {
        case a.SUIT_LED:
          return action.suit
        case a.LEAVE_TABLE:
            return '';
        default:
            break;
    }
    return state;
}

export const appReducer = combineReducers({
                    token,
                    username,
                    chats,
                    is_logged_in,
                    userlist,
                    tablelist,
                    hand,
                    seat,
                    direction_to_act,
                    auction,
                    contract,
                    trick,
                    suit_led
                    });

export const rootReducer = (state, action) => {
    if (action.type === 'LOGOUT') {
        state = undefined
    }
    return appReducer(state, action)
}
