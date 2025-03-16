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
  <salesreturnmodel></salesreturnmodel>
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
    title: "SKU",
    dataIndex: "SKU",
    key: "SKU",
    sorter: {
      compare: (a, b) => {
        a = a.SKU.toLowerCase();
        b = b.SKU.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Category",
    dataIndex: "Category",
    key: "Category",
    sorter: {
      compare: (a, b) => {
        a = a.Category.toLowerCase();
        b = b.Category.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Sold Amount",
    dataIndex: "SoldAmount",
    sorter: {
      compare: (a, b) => {
        a = a.SoldAmount.toLowerCase();
        b = b.SoldAmount.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Sold Qty",
    dataIndex: "SoldQty",
    key: "SoldQty",
    sorter: {
      compare: (a, b) => {
        a = a.SoldQty.toLowerCase();
        b = b.SoldQty.toLowerCase();
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
  },
  {
    title: "Due Date",
    dataIndex: "DueDate",
    key: "DueDate",
    sorter: {
      compare: (a, b) => {
        a = a.DueDate.toLowerCase();
        b = b.DueDate.toLowerCase();
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
    SoldQty: "50",
    SKU: "PPT001",
    InstockQty: "100",
    Category: "Laptop",
    DueDate: "20 Aug 2023",
    SoldAmount: "$8253.00",
  },
  {
    id: "2",
    Image: "sales-return2.svg",
    Name: "Nike Jordan",
    SoldQty: "70",
    SKU: "PPT005",
    InstockQty: "140",
    Category: "Shoe",
    DueDate: "23 Aug 2023",
    SoldAmount: "$1360.00",
  },
  {
    id: "3",
    Image: "sales-return3.svg",
    Name: "Apple Series 5 Watch",
    SoldQty: "30",
    SKU: "PPT010",
    InstockQty: "200",
    Category: "Accessories",
    DueDate: "25 Aug 2023",
    SoldAmount: "$724.00",
  },
  {
    id: "4",
    Image: "sales-return4.svg",
    Name: "Amazon Echo Dot ",
    SoldQty: "20",
    SKU: "PPT104",
    InstockQty: "250",
    Category: "Elecctronics",
    DueDate: "27 Aug 2023",
    SoldAmount: "$210.00",
  },
  {
    id: "5",
    Image: "sales-return5.svg",
    Name: "Lobar Handy",
    SoldQty: "40",
    SKU: "PPT050",
    InstockQty: "300",
    Category: "Furnitures",
    DueDate: "30 Aug 2023",
    SoldAmount: "$155.00",
  },
];
export default {
  data() {
    return {
      title: "Sales Return Report",
      data,
      columns,
    };
  },
};
</script>
