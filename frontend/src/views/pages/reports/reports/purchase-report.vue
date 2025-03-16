<template>
  <layout-header></layout-header>
  <layout-sidebar></layout-sidebar>
  
  <div class="page-wrapper">
    <div class="content container-fluid">
      <!-- Page Header -->
      <reportheader :title="title" />
      <!-- /Page Header -->

      <!-- Search Filter -->
      <div id="filter_inputs" class="card filter-card">
        <div class="card-body pb-0">
          <div class="row">
            <div class="col-sm-6 col-md-3">
              <div class="input-block mb-3">
                <label>Name</label>
                <input type="text" class="form-control" />
              </div>
            </div>
            <div class="col-sm-6 col-md-3">
              <div class="input-block mb-3">
                <label>Email</label>
                <input type="text" class="form-control" />
              </div>
            </div>
            <div class="col-sm-6 col-md-3">
              <div class="input-block mb-3">
                <label>Phone</label>
                <input type="text" class="form-control" />
              </div>
            </div>
          </div>
        </div>
      </div>
      <!-- /Search Filter -->

      <div class="row">
        <div class="col-sm-12">
          <div class="card-table">
            <div class="card-body">
              <div class="table-responsive">
                <a-table class="stripped table-hover" :columns="columns" :data-source="data">
                  <template #bodyCell="{ column, record }">
                    <template v-if="column.key === 'Product'">
                      <h2 class="table-avatar d-flex">
                        <router-link to="/profile" class="avatar avatar-md me-2 companies">
                          <img class="avatar-img sales-rep" :src="require(`@/assets/img/${record.Image}`)"
                            alt="User Image" /></router-link>
                        <router-link to="/profile">{{ record.Name }}</router-link>
                      </h2>
                    </template>
                  </template>
                </a-table>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <purchasemodel></purchasemodel>
</template>
<script>
const columns = [
  {
    title: "#",
    dataIndex: "id",
    sorter: {
      compare: (a, b) => {
        a = a.id.toLowerCase();
        b = b.id.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Product",
    dataIndex: "Name",
    key: "Product",
    sorter: {
      compare: (a, b) => {
        a = a.Name.toLowerCase();
        b = b.Name.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Purchase Amount",
    dataIndex: "PurchaseAmount",
    sorter: {
      compare: (a, b) => {
        a = a.PurchaseAmount.toLowerCase();
        b = b.PurchaseAmount.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Purchase Qty",
    dataIndex: "PurchaseQty",
    key: "PurchaseQty",
    sorter: {
      compare: (a, b) => {
        a = a.PurchaseQty.toLowerCase();
        b = b.PurchaseQty.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Instock Qty",
    dataIndex: "InstockQty",
    key: "InstockQty",
    sorter: {
      compare: (a, b) => {
        a = a.InstockQty.toLowerCase();
        b = b.InstockQty.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  }
];
const data = [
  {
    id: "1",
    Image: "sales-return1.svg",
    Name: "Lenovo 3rd Generation",
    PurchaseQty: "50",
    InstockQty: "100",
    PurchaseAmount: "$7248.00",
  },
  {
    id: "2",
    Image: "sales-return2.svg",
    Name: "Nike Jordan",
    PurchaseQty: "70",
    InstockQty: "140",
    PurchaseAmount: "$1350.00",
  },
  {
    id: "3",
    Image: "sales-return3.svg",
    Name: "Apple Series 5 Watch",
    PurchaseQty: "30",
    InstockQty: "200",
    PurchaseAmount: "$700.00",
  },
  {
    id: "4",
    Image: "sales-return4.svg",
    Name: "Amazon Echo Dot ",
    PurchaseQty: "20",
    InstockQty: "250",
    PurchaseAmount: "$200.00",
  },
  {
    id: "5",
    Image: "sales-return5.svg",
    Name: "Lobar Handy",
    PurchaseQty: "40",
    InstockQty: "300",
    PurchaseAmount: "$150.00",
  },
];
export default {
  data() {
    return {
      title: "Purchase Report",
      data,
      columns,
    };
  },
};
</script>
