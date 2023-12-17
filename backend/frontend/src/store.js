import { createStore, combineReducers, applyMiddleware } from "redux";
import thunk from "redux-thunk";
import {
  productListReducers,
  productDetailReducers,
  productCreateReducers,
} from "./reducers/productReducers";
import { cartReducers } from "./reducers/cartReducers";
import {
  userLoginReducers,
  userRegisterReducers,
  userDetailReducers,
  userUpdateProfileReducers,
} from "./reducers/userReducers";
import { composeWithDevTools } from "redux-devtools-extension";
import {
  orderCreateReducers,
  orderDetailsReducers,
} from "./reducers/orderReducers";

const reducer = combineReducers({
  productList: productListReducers,
  productDetail: productDetailReducers,
  cart: cartReducers,
  userLogin: userLoginReducers,
  userRegister: userRegisterReducers,
  userDetail: userDetailReducers,
  userUpdateProfile: userUpdateProfileReducers,
  orderCreate: orderCreateReducers,
  orderDetails: orderDetailsReducers,
  productCreate: productCreateReducers,
});

const cartItemsFromStorage = localStorage.getItem("cartItems")
  ? JSON.parse(localStorage.getItem("cartItems"))
  : [];

const userInfoFromStorage = localStorage.getItem("userInfo")
  ? JSON.parse(localStorage.getItem("userInfo"))
  : null;

const shippingAddressFromStorage = localStorage.getItem("shippingAddress")
  ? JSON.parse(localStorage.getItem("shippingAddress"))
  : {};

const initialState = {
  cart: {
    cartItems: cartItemsFromStorage,
    shippingAddress: shippingAddressFromStorage,
  },
  userLogin: { userInfo: userInfoFromStorage },
};

const middleware = [thunk];
const store = createStore(
  reducer,
  initialState,
  composeWithDevTools(applyMiddleware(...middleware))
);

export default store;
