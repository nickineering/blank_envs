import * as React from "react";
import { Link, Outlet } from "react-router-dom";

export function Root() {
  return (
    <main className="container">
      <nav>
        <ul>
          <li>
            <Link to="/">Home</Link>
          </li>
          <li>
            <Link to="/about">About</Link>
          </li>
        </ul>
      </nav>

      <hr />

      <Outlet />
    </main>
  );
}
