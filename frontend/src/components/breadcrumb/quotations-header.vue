<template>
  <div class="page-header">
    <div class="content-page-header">
      <h5>{{ title }}</h5>
      <div class="list-btn">
        <ul class="filter-list">
          <li>
            <a
              class="btn btn-filters w-auto popup-toggle"
              data-bs-toggle="tooltip"
              data-bs-placement="bottom"
              title="Filter"
              ><span class="me-2"
                ><img src="@/assets/img/icons/filter-icon.svg" alt="Filter" /></span
              >Filter
            </a>
          </li>
          <li>
            <a
              class="btn-filters"
              href="javascript:void(0);"
              data-bs-toggle="tooltip"
              data-bs-placement="bottom"
              title="Settings"
              ><span><i class="feather feather-settings"></i></span>
            </a>
          </li>
          <li v-if="isQuatationsRoute">
            <router-link class="btn btn-primary" to="add-quotations"
              ><i class="fa fa-plus-circle me-2" aria-hidden="true"></i
              >{{ text }}</router-link
            >
          </li>
          <li v-if="isDeliveryRoute">
            <router-link class="btn btn-primary" to="/quotations/add-delivery-challans"
              ><i class="fa fa-plus-circle me-2" aria-hidden="true"></i
              >{{ text }}</router-link
            >
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  props: {
    title: {
      type: String,
      default: "",
    },
    text: {
      type: String,
      default: "",
    },
  },
  data() {
    return {};
  },
  computed: {
    isQuatationsRoute() {
      return this.$route.path === "/quotations/quotations-list";
    },
    isDeliveryRoute() {
      return this.$route.path === "/quotations/delivery-challans";
    },
  },
};
</script>
