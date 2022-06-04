module.exports = {
  content: [
    "./pages/**/*.{html,js, jsx}",
    "./components/**/*.{html,js, jsx}",
    "./index.html",
    "./public/index.html",
    "./src/**/*.{html,js}",
  ],
  plugins: [],
  corePlugins: {
    preflight: false,
  },
  prefix: "tw-",
  important: true,
  theme: {
    // || Here sizes can be configuered down under screens to match ||
    // || any css framework sizes(Here:  Bootstrap breakpoints - 1) ||
    // || https://tailwindcss.com/docs/configuration ||
    screens: {
      sm: "575px",
      md: "767px",
      lg: "991px",
      xl: "1199",
      "2xl": "1399",
    },
    extend: {
      colors: {
        highlight: "#FF6B00",
      },
    },
  },
};
