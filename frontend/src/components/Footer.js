import React from "react";

function Footer() {
  return (
    <div className="tw-bg-gray-900 ">
      <footer className="py-3 my-4">
        <ul className="nav justify-content-center border-bottom pb-3 mb-3">
          <li className="nav-item">
            <a href="/about" className="nav-link px-2 text-muted">
              <span className="bg-gray-900 text-white">Home</span>
            </a>
          </li>
          <li className="nav-item">
            <a href="/about" className="nav-link px-2 text-muted">
              <span className="bg-gray-900 text-white">About</span>
            </a>
          </li>
          <li className="nav-item">
            <a href="/about" className="nav-link px-2 text-muted">
              <span className="bg-gray-900 text-white">FAQs</span>
            </a>
          </li>
          <li className="nav-item">
            <a href="/about" className="nav-link px-2 text-muted">
              <span className="bg-gray-900 text-white">Inquires</span>
            </a>
          </li>
        </ul>
        <p className="text-center text-muted">© 2022 | Sprints.io | Inc</p>
        <p></p>
      </footer>
    </div>
  );
}

export default Footer;
