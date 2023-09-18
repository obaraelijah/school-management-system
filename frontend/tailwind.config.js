/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{html,js,jsx}'],
  theme: {
    extend: {
      colors: {
        'custom-green': {
          100: '#2071B2',
        },
        'cm-orange': {
          100: '#F48C06',
        },
        header: '#001C27',
        btn: '#49BBBD',
        'light-btn': 'rgba(73, 187, 189, 0.60)',
      },
      backgroundColor: {
        'custom-green': {
          100: '#2071B2',
        },
        header: '#001C27',
        dashboard: {
          100: '#111827',
          200: '#ff9900',
        },
        btn: '#49BBBD',
        light: 'rgba(255, 255, 255, 0.30)',
      },
      padding: {
        sm: '0.625rem',
        base: '0.9375rem',
      },
      backgroundImage: {
        hero: 'linear-gradient(rgba(0,0,0,0.8),rgba(0,0,0,0.2)),url("/hero.webp")',
      },
      boxShadow: {
        hero: '0px 4px 100px 0px rgba(29, 28, 24, 0.25)',
      },
    },
  },
  plugins: [],
};
