<template>
  <layout-header></layout-header>
  <layout-sidebar></layout-sidebar>
  
    <!-- Page Wrapper -->
    <div class="page-wrapper">
      <div class="content container-fluid">
        <!-- Page Header -->
        <inventory-historyheader />
        <!-- /Page Header -->

        <!-- Table -->
        <div class="row">
          <div class="col-sm-12">
            <div class="card-table">
              <div class="card-body">
                <div class="table-responsive">
                  <div class="inventory-table">
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
                                    <a class="dropdown-item" href="javascript:;"
                                      ><i class="far fa-edit me-2"></i>Edit</a
                                    >
                                  </li>
                                  <li>
                                    <a
                                      class="dropdown-item"
                                      href="javascript:;"
                                      data-bs-toggle="modal"
                                      data-bs-target="#delete_modal"
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
        </div>
        <!-- /Table -->
      </div>
    </div>
    <!-- /Page Wrapper -->
  <inventorymodel />

  <delete-modal :DeleteTitle="DeleteTitle" />
</template>

<script>
const columns = [
  {
    title: "#",
    dataIndex: "id",
    sorter: {
      compare: (a, b) => {
        a = a.Code.toLowerCase();
        b = b.Code.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Item",
    key: "Item",
    dataIndex: "Item",
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
    class: "text-center",
  },
];

const data = [
  {
    id: "1",
    Item: "Nike Jordan",
    Code: "P125390",
    Units: "Pieces",
    Quantity: "2",
    SellingPrice: "$1360.00",
    PurchasePrice: "$1350.00",
  },
  {
    id: "2",
    Item: "Lobar Handy",
    Code: "P125393",
    Units: "Inches",
    Quantity: "5",
    SellingPrice: "$155.00",
    PurchasePrice: "$150.00",
  },
  {
    id: "3",
    Item: "Iphone 14 Pro",
    Code: "P125398",
    Units: "Inches",
    Quantity: "7",
    SellingPrice: "$764.00",
    PurchasePrice: "$750.00",
  },
  {
    id: "4",
    Item: "Black Slim 200",
    Code: "P125395",
    Units: "Inches",
    Quantity: "3",
    SellingPrice: "$255.00",
    PurchasePrice: "$250.00",
  },
  {
    id: "5",
    Item: "Bold V3.2",
    Code: "P125397",
    Units: "Pieces",
    Quantity: "6",
    SellingPrice: "$1055.00",
    PurchasePrice: "$1050.00",
  },
  {
    id: "6",
    Item: "Woodcraft Sandal",
    Code: "P125394",
    Units: "Pieces",
    Quantity: "8",
    SellingPrice: "$175.00",
    PurchasePrice: "$140.00",
  },
];
export default {
  data() {
    return {
      columns,
      data,
      DeleteTitle: "Delete Inventory History",
    };
  },
};
</script>
