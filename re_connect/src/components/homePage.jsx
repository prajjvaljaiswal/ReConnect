"use client";
import { useDispatch, useSelector } from "react-redux";
import { addUser, removeUser } from "@/utils/userSlice";
import { useEffect, useState } from "react";
import { Input } from "@/components/ui/input"
import { Button } from "./ui/button";



export default function HomePage() {
  const dispatch = useDispatch();
  const { user, isLogedIn } = useSelector((state) => state.user);
  const [ show, setShow ] = useState(false);
  const [rest, setRest] = useState(false);
  const [email, setEmail] = useState("");
  const baseUrl = "http://127.0.0.1:8000";

  const fetchUser = async () => {
    try {
        const response = await fetch(baseUrl + "/users/"+email);
        const data = await response.json();
        return data;
    } catch (error) {
        console.error("Failed to fetch user", error);
    }
};

//   useEffect(() => {
//     if (isLogedIn) {
//       setShow(true);
//     }
//     else{
//         // const user = fetchUser();
//         console.log(email);
//         setShow(true);
//         dispatch(addUser(user));
//     }
//     return () => {
//       dispatch(removeUser());
//         setShow(false);
//     };
//   }, []);
     const handelSubmit=async()=>{
        const user = await fetchUser();
        console.log(user);
        dispatch(addUser(user));
    }
  return (
    <div>
        <Input onChange={(e)=> setEmail(e.target.value)}/>
        <Button onClick={()=> handelSubmit()}>submit</Button>
      <div>{isLogedIn ? <h1> Logedin</h1> : <h1>not Logedin</h1>}</div>
    </div>
  );
}
