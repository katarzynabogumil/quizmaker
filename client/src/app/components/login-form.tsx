'use client';

import { FormEvent } from "react";
import { Button, TextField } from "@mui/material";
import { login } from "../services/auth.service";
// import styles from '@/styles/LoginForm.module.css';

export default function LoginForm() {

  async function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault()
    const target = event.target as typeof event.target & {
      username: { value: string };
      password: { value: string };
    };

    const data = {
      username: target.username.value,
      password: target.password.value,
    }

    login(data);
  }

  /* <div className={styles.inputContainer}> */
  return (
    <form 
      className="flex min-h-screen flex-col items-center justify-between p-24"
      onSubmit={handleSubmit} 
    >
      <TextField 
        id="outlined-username"
        label="Username" 
        name="username"
        required={true}
      />
      <TextField
        id="outlined-password-input"
        label="Password"
        name="password"
        type="password"
        autoComplete="current-password"
        required={true}
      />
      <Button 
        variant="outlined" 
        color="primary"
        type="submit"
      >
        Login
      </Button>
    </form>
  );
}
