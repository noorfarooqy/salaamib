<template>
  <layout-header></layout-header>
  <layout-sidebar></layout-sidebar>
  
    <!-- Page Wrapper -->
    <div class="page-wrapper">
      <div class="content container-fluid">
        <!-- Page Header -->
        <div class="page-header">
          <div class="content-page-header">
            <h5>Permission</h5>
          </div>
          <div class="role-testing d-flex align-items-center justify-content-between">
            <h6>Role Name:<span class="ms-1">Testings</span></h6>
            <p>
              <label class="custom_check"
                ><input type="checkbox" name="invoice" /><span
                  class="checkmark"
                ></span></label
              >Allow All Modules
            </p>
          </div>
        </div>
        <!-- /Page Header -->

        <!-- Table -->
        <div class="row">
          <div class="col-sm-12">
            <div class="card-table">
              <div class="card-body">
                <div class="table-responsive">
                  <table class="table table-stripped table-hover">
                    <thead class="thead-light">
                      <tr>
                        <th>#</th>
                        <th>Modules</th>
                        <th>Sub Modules</th>
                        <th>Create</th>
                        <th>Edit</th>
                        <th>Delete</th>
                        <th>View</th>
                        <th>Allow all</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr v-for="item in permission" :key="item.id">
                        <td>{{ item.id }}</td>
                        <td class="role-data">{{ item.Modules }}</td>
                        <td>{{ item.SubModules }}</td>
                        <td>
                          <label class="custom_check">
                            <input type="checkbox" name="invoice" />
                            <span class="checkmark"></span>
                          </label>
                        </td>
                        <td>
                          <label class="custom_check">
                            <input type="checkbox" name="invoice" />
                            <span class="checkmark"></span>
                          </label>
                        </td>
                        <td>
                          <label class="custom_check">
                            <input type="checkbox" name="invoice" />
                            <span class="checkmark"></span>
                          </label>
                        </td>
                        <td>
                          <label class="custom_check">
                            <input type="checkbox" name="invoice" />
                            <span class="checkmark"></span>
                          </label>
                        </td>
                        <td>
                          <label class="custom_check">
                            <input type="checkbox" name="invoice" />
                            <span class="checkmark"></span>
                          </label>
                        </td>
                      </tr>
                    </tbody>
                  </table>
                </div>
              </div>
            </div>
          </div>
        </div>
        <!-- /Table -->

        <div class="text-center">
          <button type="submit" class="btn btn-primary cancel me-2">Back</button>
          <b-button type="submit" variant="primary">Update</b-button>
        </div>
      </div>
    </div>
    <!-- /Page Wrapper -->
</template>
<script>
import permission from "@/assets/json/permission.json";
export default {
  setup() {
    return {
      permission: permission,
    };
  },
};
</script>
