import * as React from "react";
import { Link } from "react-router-dom";

export default function ErrorPage() {
  return (
    <div>
      <h2>Oops!</h2>
      <p>
        Page not found. Please go <Link to="/">home</Link> and try again.
      </p>
    </div>
  );
}
