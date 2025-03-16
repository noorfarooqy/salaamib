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
                <a-table
                  class="stripped table-hover"
                  :columns="columns"
                  :data-source="data"
                >
                  <template #bodyCell="{ column, record }">
                    <template v-if="column.key === 'Product'">
                      <h2 class="table-avatar d-flex">
                        <router-link
                          to="/profile"
                          class="avatar avatar-md me-2 companies"
                        >
                          <img
                            class="avatar-img sales-rep"
                            :src="require(`@/assets/img/${record.Image}`)"
                            alt="User Image"
                        /></router-link>
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
  <lowstockmodel></lowstockmodel>
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
    title: "Opening Qty",
    dataIndex: "OpeningQty",
    sorter: {
      compare: (a, b) => {
        a = a.OpeningQty.toLowerCase();
        b = b.OpeningQty.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Closing Qty",
    dataIndex: "ClosingQty",
    sorter: {
      compare: (a, b) => {
        a = a.ClosingQty.toLowerCase();
        b = b.ClosingQty.toLowerCase();
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
    OpeningQty: "0",
    SKU: "PPT001",
    Category: "Laptop",
    ClosingQty: "5",
  },
  {
    id: "2",
    Image: "sales-return2.svg",
    Name: "Nike Jordan",
    OpeningQty: "0",
    SKU: "PPT005",
    Category: "Shoe",
    ClosingQty: "10",
  },
  {
    id: "3",
    Image: "sales-return3.svg",
    Name: "Apple Series 5 Watch",
    OpeningQty: "0",
    SKU: "PPT010",
    Category: "Accessories",
    ClosingQty: "5",
  },
  {
    id: "4",
    Image: "sales-return4.svg",
    Name: "Amazon Echo Dot ",
    OpeningQty: "0",
    SKU: "PPT104",
    Category: "Elecctronics",
    ClosingQty: "10",
  },
  {
    id: "5",
    Image: "sales-return5.svg",
    Name: "Lobar Handy",
    OpeningQty: "0",
    SKU: "PPT050",
    Category: "Furnitures",
    ClosingQty: "10",
  },
];
export default {
  data() {
    return {
      title: "Low Stock Report",
      data,
      columns,
    };
  },
};
</script>
