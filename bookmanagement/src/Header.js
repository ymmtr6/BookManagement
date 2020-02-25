import React from "react";

export function Header() {
  return (
    <div className="Header shadow-md text-center">
      <img className="w-2/12 hvr-wobble-horizontal" src={`${process.env.PUBLIC_URL}/img/logo.png`} alt="Logo" />
    </div>
  );
}
