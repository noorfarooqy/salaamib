<template>
  <layout-header></layout-header>
  <layout-sidebar></layout-sidebar>
  

  <!-- Page Wrapper -->
  <div class="page-wrapper">
    <div class="content container-fluid">
      <inventoryheader />

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
                    <template v-if="column.key === 'PurchasePrice'">
                      <div>{{ record.PurchasePrice }}</div>
                    </template>
                    <template v-else-if="column.key === 'Action'">
                      <div class="d-flex align-items-center">
                        <router-link
                          to="inventory-history"
                          class="btn btn-greys bg-history-light me-2"
                        >
                          <i class="far fa-eye me-1"></i> History
                        </router-link>
                        <a
                          href="javascript:;"
                          class="btn btn-greys bg-success-light me-2"
                          data-bs-toggle="modal"
                          data-bs-target="#stock_in"
                        >
                          <i class="fa fa-plus-circle me-1"></i> Stock in
                        </a>
                        <a
                          href="javascript:;"
                          class="btn btn-greys bg-danger-light me-2"
                          data-bs-toggle="modal"
                          data-bs-target="#stock_out"
                        >
                          <i class="fa fa-plus-circle me-1"></i> Stock out
                        </a>
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
                                <a
                                  class="dropdown-item"
                                  href="javascript:void(0);"
                                  data-bs-toggle="modal"
                                  data-bs-target="#edit_inventory"
                                  ><i class="far fa-edit me-2"></i>Edit</a
                                >
                              </li>
                              <li>
                                <a
                                  class="dropdown-item"
                                  href="javascript:;"
                                  data-bs-toggle="modal"
                                  data-bs-target="#delete_stock"
                                  ><i class="far fa-trash-alt me-2"></i>Delete</a
                                >
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

  <inventorymodel />
</template>

<script>
const columns = [
  {
    title: "#",
    dataIndex: "NUM",
    sorter: (a, b) => a.NUM.localeCompare(b.NUM),
  },
  {
    title: "Item",
    key: "Item",
    dataIndex: "Item",
    sorter: (a, b) => a.Item.localeCompare(b.Item),
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
    title: "Units",
    dataIndex: "Units",
    sorter: (a, b) => a.Units.localeCompare(b.Units),
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
    title: "Sales Price",
    dataIndex: "SalesPrice",
    sorter: {
      compare: (a, b) => {
        a = a.SalesPrice.toLowerCase();
        b = b.SalesPrice.toLowerCase();
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
    class: "text-center",
  },
];
const data = [
  {
    NUM: "1",
    Item: "Lenovo 3rd Generation",
    Code: "P125389",
    Units: "Inches",
    Quantity: "2",
    SalesPrice: "$253.00",
    PurchasePrice: "$248.00",
  },
  {
    NUM: "2",
    Item: "Nike Jordan",
    Code: "P125390",
    Units: "Pieces",
    Quantity: "4",
    SalesPrice: "$360.00",
    PurchasePrice: "$350.00",
  },
  {
    NUM: "3",
    Item: "Apple Series 5 Watch",
    Code: "P125391",
    Units: "Inches",
    Quantity: "7",
    SalesPrice: "$724.00",
    PurchasePrice: "$700.00",
  },
  {
    NUM: "4",
    Item: "Amazon Echo Dot",
    Code: "P125392",
    Units: "Box",
    Quantity: "3",
    SalesPrice: "$210.00",
    PurchasePrice: "$200.00",
  },
  {
    NUM: "5",
    Item: "Lobar Handy",
    Code: "P125393",
    Units: "Kilograms",
    Quantity: "1",
    SalesPrice: "$155.00",
    PurchasePrice: "$150.00",
  },
  {
    NUM: "6",
    Item: "Woodcraft Sandal",
    Code: "P125389",
    Units: "Inches",
    Quantity: "2",
    SalesPrice: "$253.00",
    PurchasePrice: "$248.00",
  },
];
export default {
  setup() {
    return {
      data,
      columns,
    };
  },
};
</script>
