import ShopButton from '../components/ShopButton';

function Shop() {
    return (
        <div>
            <h1 style={{textAlign: "center"}}>Shop</h1>
            <table style={{marginLeft: "80px"}}>
                <tr>
                    <td>
                        <ShopButton type="Toys"/>
                    </td>
                    <td>
                        <ShopButton type="Food"/>
                    </td>
                    <td>
                        <ShopButton type="Beds"/>
                    </td>
                    <td>
                        <ShopButton type="Accessories"/>
                    </td>
                </tr>
            </table>
        </div>
    )
}

export default Shop;