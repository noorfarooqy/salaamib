<template>
  <layout-header></layout-header>
  <layout-sidebar></layout-sidebar>
  
    <!-- Page Wrapper -->
    <div class="page-wrapper">
      <div class="content container-fluid">
        <productlistheader />

        <!-- Search Filter -->
        <div id="filter_inputs" class="card filter-card">
          <div class="card-body pb-0">
            <div class="row">
              <div class="col-sm-6 col-md-3">
                <div class="form-group">
                  <label>Name</label>
                  <input type="text" class="form-control" />
                </div>
              </div>
              <div class="col-sm-6 col-md-3">
                <div class="form-group">
                  <label>Email</label>
                  <input type="text" class="form-control" />
                </div>
              </div>
              <div class="col-sm-6 col-md-3">
                <div class="form-group">
                  <label>Phone</label>
                  <input type="text" class="form-control" />
                </div>
              </div>
            </div>
          </div>
        </div>
        <!-- /Search Filter -->

        <!-- All Invoice -->
        <div class="card invoices-tabs-card">
          <div class="invoices-main-tabs">
            <div class="row align-items-center">
              <div class="col-lg-12">
                <div class="invoices-tabs">
                  <ul>
                    <li>
                      <router-link to="product-list" class="active">Product</router-link>
                    </li>
                    <li>
                      <router-link to="category">Category</router-link>
                    </li>
                    <li>
                      <router-link to="units">Units</router-link>
                    </li>
                  </ul>
                </div>
              </div>
            </div>
          </div>
        </div>
        <!-- /All Invoice -->

        <!-- Table -->
        <div class="row">
          <div class="col-sm-12">
            <div class="card-table">
              <div class="card-body">
                <div class="table-responsive">
                  <a-table
                    class="stripped table-hover"
                    :columns="columns"
                    :data-source="data"
                  >
                    <template #bodyCell="{ column, record }">
                      <template v-if="column.key === 'Item'">
                        <div>
                          <a href="javascript:;" class="product-list-item-img">
                            <img
                              :src="require(`@/assets/img/${record.Img}`)"
                              alt="product-list"
                            />
                            <span>{{ record.Item }}</span>
                          </a>
                        </div>
                      </template>
                      <template v-if="column.key === 'PurchasePrice'">
                        <div>{{ record.PurchasePrice }}</div>
                      </template>
                      <template v-else-if="column.key === 'Action'">
                        <div class="d-flex align-items-center">
                          <div class="dropdown dropdown-action">
                            <a
                              href="javascript:;"
                              class="btn-action-icon"
                              data-bs-toggle="dropdown"
                              aria-expanded="false"
                              ><i class="fas fa-ellipsis-v"></i
                            ></a>
                            <div class="dropdown-menu dropdown-menu-right">
                              <ul>
                                <li>
                                  <router-link class="dropdown-item" to="/product-service/edit-products"
                                    ><i class="far fa-edit me-2"></i>Edit</router-link
                                  >
                                </li>
                                <li>
                                  <a
                                    class="dropdown-item"
                                    href="javascript:;"
                                    data-bs-toggle="modal"
                                    data-bs-target="#delete_modal"
                                    ><i class="far fa-trash-alt me-2"></i>Delete
                                  </a>
                                </li>
                              </ul>
                            </div>
                          </div>
                        </div>
                      </template>
                    </template>
                  </a-table>
                </div>
              </div>
            </div>
          </div>
        </div>
        <!-- /Table -->
      </div>
    </div>
    <!-- /Page Wrapper -->
  <locationmodal :Delete="Delete" />
</template>

<script>
const columns = [
  {
    title: "#",
    dataIndex: "NUM",
    sorter: {
      compare: (a, b) => {
        a = a.NUM.toLowerCase();
        b = b.NUM.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Item",
    dataIndex: "Item",
    key: "Item",
    sorter: {
      compare: (a, b) => {
        a = a.Item.toLowerCase();
        b = b.Item.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Code",
    dataIndex: "Code",
    sorter: {
      compare: (a, b) => {
        a = a.Code.toLowerCase();
        b = b.Code.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Category",
    dataIndex: "Category",
    sorter: {
      compare: (a, b) => {
        a = a.Category.toLowerCase();
        b = b.Category.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Units",
    dataIndex: "Units",
    sorter: {
      compare: (a, b) => {
        a = a.Units.toLowerCase();
        b = b.Units.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Quantity",
    dataIndex: "Quantity",
    sorter: {
      compare: (a, b) => {
        a = a.Quantity.toLowerCase();
        b = b.Quantity.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Selling Price",
    dataIndex: "SellingPrice",
    sorter: {
      compare: (a, b) => {
        a = a.SellingPrice.toLowerCase();
        b = b.SellingPrice.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Purchase Price",
    dataIndex: "PurchasePrice",
    key: "PurchasePrice",
    sorter: {
      compare: (a, b) => {
        a = a.PurchasePrice.toLowerCase();
        b = b.PurchasePrice.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Action",
    key: "Action",
    sorter: true,
  },
];
const data = [
  {
    NUM: "1",
    Item: "Lenovo 3rd Generation",
    Img: "sales-return1.svg",
    Code: "P125389",
    Category: "Laptop",
    Units: "Inches",
    Quantity: "2",
    SellingPrice: "$253.00",
    PurchasePrice: "$248.00",
  },
  {
    NUM: "2",
    Item: "Nike Jordan",
    Img: "sales-return2.svg",
    Code: "P125390",
    Category: "Shoes",
    Units: "Pieces",
    Quantity: "4",
    SellingPrice: "$360.00",
    PurchasePrice: "$350.00",
  },
  {
    NUM: "3",
    Item: "Apple Series 5 Watch",
    Img: "sales-return3.svg",
    Code: "P125391",
    Category: "Accessories",
    Units: "Inches",
    Quantity: "7",
    SellingPrice: "$724.00",
    PurchasePrice: "$700.00",
  },
  {
    NUM: "4",
    Item: "Amazon Echo Dot",
    Img: "sales-return4.svg",
    Code: "P125392",
    Category: "Electronics",
    Units: "Box",
    Quantity: "3",
    SellingPrice: "$210.00",
    PurchasePrice: "$200.00",
  },
  {
    NUM: "5",
    Item: "Lobar Handy",
    Img: "sales-return5.svg",
    Code: "P125393",
    Category: "Furnitures",
    Units: "Kilograms",
    Quantity: "1",
    SellingPrice: "$155.00",
    PurchasePrice: "$150.00",
  },
  {
    NUM: "6",
    Item: "Woodcraft Sandal",
    Img: "sales-return6.svg",
    Code: "P125394",
    Category: "Bags",
    Units: "Inches",
    Quantity: "2",
    SellingPrice: "$253.00",
    PurchasePrice: "$248.00",
  },
  {
    NUM: "7",
    Item: "Black Slim 200",
    Img: "sales-return7.svg",
    Code: "P125394",
    Category: "Furnitures",
    Units: "Inches",
    Quantity: "2",
    SellingPrice: "$253.00",
    PurchasePrice: "$248.00",
  },
  {
    NUM: "8",
    Item: "Red Premium Handy",
    Img: "sales-return8.svg",
    Code: "P125394",
    Category: "Bags",
    Units: "Inches",
    Quantity: "2",
    SellingPrice: "$253.00",
    PurchasePrice: "$248.00",
  },
  {
    NUM: "9",
    Item: "Bold V3.2",
    Img: "sales-return9.svg",
    Code: "P125394",
    Category: "Electronics",
    Units: "Inches",
    Quantity: "2",
    SellingPrice: "$253.00",
    PurchasePrice: "$248.00",
  },
  {
    NUM: "10",
    Item: "Iphone 14 Pro",
    Img: "sales-return10.svg",
    Code: "P125394",
    Category: "Phone",
    Units: "Inches",
    Quantity: "2",
    SellingPrice: "$253.00",
    PurchasePrice: "$248.00",
  },
];

export default {
  setup() {
    return {
      Delete: "Delete Products / Services",
      data,
      columns,
    };
  },
};
</script>
