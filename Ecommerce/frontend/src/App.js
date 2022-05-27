import {
    Home,
    CheckOut,
    Orders,
    Cart,
    AccountInfo,
    Accounts,
    About,
    ErrorPage,
    SingleProduct,
    AdminDashboard,
} from './pages'
import { Header, Footer } from './components'
import { BrowserRouter, Route, Routes } from 'react-router-dom'

function App() {
    return (
        <BrowserRouter>
            <Header />
            <Routes>
                <Route path='/' element={<Home />}></Route>
                <Route path='/About' element={<About />}></Route>
                <Route path='/*' element={<ErrorPage />}></Route>
            </Routes>
            <Footer />
        </BrowserRouter>
    )
}

export default App
